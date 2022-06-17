import datetime, time

from bs4 import BeautifulSoup

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def get_cars():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get('https://www.cars.bg/carslist.php?subm=1&add_search=1&typeoffer=1&fuelId%5B%5D=3&priceTo=2000&conditions%5B%5D=4&conditions%5B%5D=1&locationId=3&radius=1')
    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
            
    html_page = driver.page_source
    soup = BeautifulSoup(html_page, 'html.parser')
    grid = soup.find(class_='mdc-layout-grid__cell')

    cars_containers = grid.find_all(class_='mdc-layout-grid__inner')

    list_of_kwargs = []

    for container in cars_containers:
        cells = container.find_all(class_='mdc-layout-grid__cell')
        for cell in cells:
            timestamp = cell.find(class_='card__subtitle mdc-typography mdc-typography--overline')
            date = get_date(timestamp)

            img = cell.find(class_='mdc-card__media mdc-card__media--16-9')
            img_link = str(img['style']).split('"', 2)[1]

            price_cell = cell.find(class_='card__title mdc-typography mdc-typography--headline6 price')
            for i in price_cell.string.split():
                i = i.replace(',', '')
                if i.isdigit():
                    price = i

            model_cell = cell.find(class_='card__title mdc-typography mdc-typography--headline5 observable')
            description_cell = cell.find(class_='card__secondary mdc-typography mdc-typography--body1 black')
            comment_cell = cell.find(class_='card__secondary mdc-typography mdc-typography--body2')
            
            seller_cell = cell.find(class_='card__footer mdc-typography mdc-typography--body2 align-bottom')
            seller = ''
            for x in str(seller_cell.string).split():
                if x != 'None':
                    seller += x + ' '
            
            link_cell = cell.find("a", class_='d-grid no-decoration')
            link = link_cell['href']

            list_of_kwargs.append({
                'date': date,
                'img': img_link,
                'price': price,
                'model': format_string(model_cell),
                'description': format_string(description_cell),
                'comment': format_string(comment_cell),
                'seller': seller,
                'link': link
            })
    return list_of_kwargs

def format_string(cell):
    y = ''
    for x in cell.string.split():
        y += x + ' '
    return y

def get_date(timestamp):
    splitted_timestamp = str(timestamp).split()
    if 'днес,' in splitted_timestamp:
        date = ''
        hour = splitted_timestamp.pop(splitted_timestamp.index('днес,') + 1)
        date += splitted_timestamp.pop(splitted_timestamp.index('днес,'))
        date += ' ' + hour
    elif 'вчера' in splitted_timestamp:
        date = 'вчера'
    else:
        for i in splitted_timestamp:
            if validate_as_date(i):
                date = i
    return date

def validate_as_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d.%m.%y')
        return date_text
    except ValueError:
        return False

if __name__ == '__main__':
    print(get_cars())
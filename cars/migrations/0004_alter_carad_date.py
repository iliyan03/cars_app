# Generated by Django 4.0.5 on 2022-06-18 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_carad_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carad',
            name='date',
            field=models.DateTimeField(),
        ),
    ]

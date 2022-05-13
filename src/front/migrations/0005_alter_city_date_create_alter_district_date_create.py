# Generated by Django 4.0.4 on 2022-05-13 13:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0004_alter_city_date_create_alter_district_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 13, 13, 13, 40, 320221, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='district',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 13, 13, 13, 40, 320941, tzinfo=utc)),
        ),
    ]
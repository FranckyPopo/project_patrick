# Generated by Django 4.0.4 on 2022-05-13 13:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_alter_city_date_create_alter_district_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 13, 13, 12, 3, 535845, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='district',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 13, 13, 12, 3, 536597, tzinfo=utc)),
        ),
    ]

# Generated by Django 2.2.24 on 2021-07-31 05:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0018_auto_20210730_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessage',
            name='time_added',
            field=models.TimeField(default=datetime.datetime(2021, 7, 31, 5, 36, 51, 526954, tzinfo=utc)),
        ),
    ]

# Generated by Django 2.2.24 on 2021-07-30 14:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_auto_20210730_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessage',
            name='time_added',
            field=models.TimeField(default=datetime.datetime(2021, 7, 30, 14, 57, 18, 556657, tzinfo=utc)),
        ),
    ]
# Generated by Django 2.2.24 on 2021-07-31 08:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0026_auto_20210731_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessage',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 31, 8, 49, 8, 508122, tzinfo=utc)),
        ),
    ]

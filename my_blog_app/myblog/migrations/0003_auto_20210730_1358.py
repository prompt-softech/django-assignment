# Generated by Django 2.2.24 on 2021-07-30 13:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_usermessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybloguser',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='time_added',
            field=models.TimeField(default=datetime.datetime(2021, 7, 30, 13, 58, 4, 228341, tzinfo=utc)),
        ),
    ]
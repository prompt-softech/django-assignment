# Generated by Django 2.2.24 on 2021-07-30 18:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0015_auto_20210730_1852'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyBlogUser',
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='text_message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='time_added',
            field=models.TimeField(default=datetime.datetime(2021, 7, 30, 18, 54, 36, 543431, tzinfo=utc)),
        ),
    ]

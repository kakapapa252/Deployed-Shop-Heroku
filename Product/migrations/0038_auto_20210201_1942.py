# Generated by Django 3.1.5 on 2021-02-01 14:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0037_auto_20210131_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 14, 12, 45, 80895, tzinfo=utc)),
        ),
    ]
# Generated by Django 3.0.3 on 2020-05-17 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0041_auto_20200518_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='uploadTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]

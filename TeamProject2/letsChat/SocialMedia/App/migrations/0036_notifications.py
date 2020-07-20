# Generated by Django 3.0.3 on 2020-05-17 07:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0035_delete_notifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, max_length=55)),
                ('sender', models.CharField(blank=True, max_length=55)),
                ('receiver', models.CharField(blank=True, max_length=55)),
                ('notification', models.CharField(blank=True, max_length=100)),
                ('viewed', models.BooleanField()),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
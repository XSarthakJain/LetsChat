# Generated by Django 3.0.3 on 2020-06-06 19:55

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0062_groupchat'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistration',
            name='Groups',
            field=django_mysql.models.ListCharField(models.CharField(blank=True, default='', max_length=50), blank=True, max_length=10000, size=None),
        ),
    ]
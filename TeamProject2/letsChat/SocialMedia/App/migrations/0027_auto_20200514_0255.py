# Generated by Django 3.0.3 on 2020-05-13 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0026_userpost_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='Message',
            field=models.CharField(blank=True, default='', max_length=5000),
        ),
    ]

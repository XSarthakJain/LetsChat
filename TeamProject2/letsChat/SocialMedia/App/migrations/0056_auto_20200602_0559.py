# Generated by Django 3.0.3 on 2020-06-02 05:59

from django.db import migrations, models
import django.utils.timezone
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0055_auto_20200601_1108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allfriends',
            old_name='roomId',
            new_name='inboxId',
        ),
        migrations.AddField(
            model_name='messages',
            name='Users',
            field=django_mysql.models.ListCharField(models.CharField(blank=True, default='', max_length=50), default=django.utils.timezone.now, max_length=10000, size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='messages',
            name='inboxId',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]

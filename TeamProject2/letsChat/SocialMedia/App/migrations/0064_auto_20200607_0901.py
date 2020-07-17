# Generated by Django 3.0.3 on 2020-06-07 09:01

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0063_userregistration_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupId', models.CharField(blank=True, default='', max_length=50)),
                ('groupName', models.CharField(blank=True, default='', max_length=50)),
                ('Members', django_mysql.models.ListCharField(models.CharField(blank=True, default='', max_length=50), max_length=10000, size=None)),
                ('groupInfo', models.CharField(blank=True, default='', max_length=50)),
                ('groupPic', models.ImageField(blank=True, default='media/group.jpg', upload_to='media')),
            ],
        ),
        migrations.RemoveField(
            model_name='groupchat',
            name='Members',
        ),
        migrations.RemoveField(
            model_name='groupchat',
            name='groupName',
        ),
    ]

# Generated by Django 3.0.3 on 2020-05-29 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0052_auto_20200528_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='postId',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]

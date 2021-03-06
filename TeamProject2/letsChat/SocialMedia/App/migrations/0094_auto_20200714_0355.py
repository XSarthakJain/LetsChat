# Generated by Django 3.0.2 on 2020-07-14 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0093_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='groupPic',
            field=models.ImageField(blank=True, default='media/group.png', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='coverPic',
            field=models.ImageField(default='media/cover.jpeg', upload_to='media'),
        ),
    ]

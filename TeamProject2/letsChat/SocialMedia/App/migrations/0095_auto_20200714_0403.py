# Generated by Django 3.0.2 on 2020-07-14 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0094_auto_20200714_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='coverPic',
            field=models.ImageField(default='media/cover.jpg', upload_to='media'),
        ),
    ]

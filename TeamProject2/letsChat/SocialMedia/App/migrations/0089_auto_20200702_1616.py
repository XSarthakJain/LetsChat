# Generated by Django 3.0.2 on 2020-07-02 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0088_albumimagedata_createalbum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='groupId',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]

# Generated by Django 3.0.2 on 2020-07-06 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0090_auto_20200705_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='dOB',
            field=models.DateField(blank=True, null=True),
        ),
    ]
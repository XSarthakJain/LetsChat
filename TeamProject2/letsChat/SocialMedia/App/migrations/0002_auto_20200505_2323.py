# Generated by Django 3.0.3 on 2020-05-05 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistration',
            name='Image',
            field=models.ImageField(default='media/profile.jpeg', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='emailAddress',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='firstName',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='lastName',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='mobile',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='userId',
            field=models.CharField(default='', max_length=50),
        ),
    ]

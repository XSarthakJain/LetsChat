# Generated by Django 3.0.3 on 2020-05-07 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_auto_20200507_0220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postId', models.CharField(max_length=100)),
                ('postLikes', models.IntegerField()),
            ],
        ),
    ]

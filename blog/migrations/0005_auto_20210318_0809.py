# Generated by Django 3.1.6 on 2021-03-18 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210304_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpost',
            name='author',
        ),
        migrations.AlterField(
            model_name='userpost',
            name='label',
            field=models.CharField(default='no Label', max_length=200),
        ),
    ]

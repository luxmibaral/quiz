# Generated by Django 3.1.6 on 2021-03-04 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210304_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='dateUpdate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

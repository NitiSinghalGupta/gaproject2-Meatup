# Generated by Django 2.0.5 on 2018-08-01 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meatup', '0005_auto_20180801_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile_pic',
        ),
    ]
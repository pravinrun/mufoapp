# Generated by Django 4.2.2 on 2023-12-14 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0002_top_fan_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='top_fan_list',
            name='sender',
        ),
    ]
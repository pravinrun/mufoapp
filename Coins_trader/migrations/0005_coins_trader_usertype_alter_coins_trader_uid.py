# Generated by Django 4.2.2 on 2023-08-27 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coins_trader', '0004_coins_trader_coins'),
    ]

    operations = [
        migrations.AddField(
            model_name='coins_trader',
            name='usertype',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='coins_trader',
            name='uid',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

# Generated by Django 4.2.2 on 2023-12-12 10:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0023_jockeyclubownerlogin_coinsclubownerdaliylogin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=200, verbose_name='Payment ID')),
                ('order_id', models.CharField(max_length=200, verbose_name='Order ID')),
                ('signature', models.CharField(max_length=500, verbose_name='Signature')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]

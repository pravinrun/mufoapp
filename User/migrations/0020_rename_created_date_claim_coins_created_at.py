# Generated by Django 4.2.2 on 2023-11-21 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0019_rename_created_at_claim_coins_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claim_coins',
            old_name='created_date',
            new_name='created_at',
        ),
    ]

# Generated by Django 4.0.1 on 2023-06-29 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Audio_Jockey', '0002_audio_jockey_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio_jockey',
            name='token',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]

# Generated by Django 4.2.2 on 2023-09-20 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0006_common_is_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social_media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Google', models.CharField(max_length=100)),
                ('Facebook', models.CharField(max_length=100)),
                ('Snapchat', models.CharField(max_length=100)),
            ],
        ),
    ]
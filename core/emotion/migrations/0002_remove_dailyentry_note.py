# Generated by Django 4.2.21 on 2025-05-26 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emotion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyentry',
            name='note',
        ),
    ]

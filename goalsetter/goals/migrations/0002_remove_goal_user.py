# Generated by Django 5.0.3 on 2024-03-29 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='user',
        ),
    ]

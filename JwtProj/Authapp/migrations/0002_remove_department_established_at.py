# Generated by Django 4.1.5 on 2023-08-23 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='established_at',
        ),
    ]

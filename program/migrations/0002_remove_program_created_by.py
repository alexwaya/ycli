# Generated by Django 2.2.1 on 2021-01-09 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='created_by',
        ),
    ]
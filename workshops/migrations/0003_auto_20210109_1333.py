# Generated by Django 2.2.1 on 2021-01-09 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0002_auto_20210109_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='content',
        ),
        migrations.RemoveField(
            model_name='application',
            name='experience',
        ),
    ]

# Generated by Django 2.2.1 on 2021-01-07 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0002_auto_20210107_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='description',
            field=models.TextField(),
        ),
    ]
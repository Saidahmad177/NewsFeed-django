# Generated by Django 4.1.6 on 2023-02-16 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_delete_modelyangi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newmodel',
            name='age',
        ),
    ]

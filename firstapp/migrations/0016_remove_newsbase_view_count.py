# Generated by Django 4.1.6 on 2023-03-11 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0015_newsbase_view_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsbase',
            name='view_count',
        ),
    ]

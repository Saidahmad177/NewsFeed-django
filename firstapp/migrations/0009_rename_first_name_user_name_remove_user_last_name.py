# Generated by Django 4.1.6 on 2023-02-26 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0008_user_delete_newmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]

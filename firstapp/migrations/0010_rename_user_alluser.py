# Generated by Django 4.1.6 on 2023-02-26 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0009_rename_first_name_user_name_remove_user_last_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='AllUser',
        ),
    ]
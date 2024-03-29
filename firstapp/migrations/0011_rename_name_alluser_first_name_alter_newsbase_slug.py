# Generated by Django 4.1.6 on 2023-03-02 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0010_rename_user_alluser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alluser',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AlterField(
            model_name='newsbase',
            name='slug',
            field=models.SlugField(max_length=30),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-14 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0018_alter_newsbase_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsbase',
            options={'ordering': ['-publish_time']},
        ),
    ]
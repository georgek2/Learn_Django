# Generated by Django 3.2.4 on 2022-03-09 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_output'),
    ]

    operations = [
        migrations.RenameField(
            model_name='output',
            old_name='apps',
            new_name='applications',
        ),
    ]
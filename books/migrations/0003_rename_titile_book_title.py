# Generated by Django 4.0.1 on 2022-01-23 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_post_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='titile',
            new_name='title',
        ),
    ]
# Generated by Django 3.2.4 on 2021-06-24 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='discription',
            new_name='description',
        ),
    ]

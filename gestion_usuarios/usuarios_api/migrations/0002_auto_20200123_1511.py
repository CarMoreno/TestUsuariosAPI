# Generated by Django 2.2 on 2020-01-23 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuarios',
            new_name='Usuario',
        ),
    ]
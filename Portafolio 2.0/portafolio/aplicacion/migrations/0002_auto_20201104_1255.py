# Generated by Django 3.1.2 on 2020-11-04 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acompañante',
            old_name='cli_cliente',
            new_name='user',
        ),
    ]
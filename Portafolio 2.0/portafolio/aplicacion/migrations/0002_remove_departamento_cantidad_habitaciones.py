# Generated by Django 3.1.2 on 2020-11-19 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departamento',
            name='cantidad_habitaciones',
        ),
    ]

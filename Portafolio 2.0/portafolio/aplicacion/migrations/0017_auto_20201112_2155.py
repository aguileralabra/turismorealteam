# Generated by Django 3.1.2 on 2020-11-13 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0016_remove_reserva_codigo_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='Estado_Reserva',
            field=models.CharField(max_length=100),
        ),
    ]

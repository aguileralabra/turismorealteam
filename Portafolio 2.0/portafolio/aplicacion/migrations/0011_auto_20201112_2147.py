# Generated by Django 3.1.2 on 2020-11-13 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0010_reserva_codigo_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='Codigo_Reserva',
            field=models.CharField(blank=True, default='000000', max_length=6),
        ),
    ]

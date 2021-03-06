# Generated by Django 3.1.2 on 2020-11-11 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0006_user_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='Estado_Reserva',
            field=models.CharField(choices=[('VIGENTE', 'VIGENTE'), ('CONCRETADA', 'CONCRETADA')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='aire_acondicionado',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=30, verbose_name='Color Vehiculo'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='disponibilidad_vehi',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=30, verbose_name='Color Vehiculo'),
        ),
    ]

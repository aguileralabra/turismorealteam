# Generated by Django 3.1.2 on 2020-11-13 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0017_auto_20201112_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='Codigo_Reserva',
            field=models.CharField(blank=True, default='', max_length=6),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='Estado_Reserva',
            field=models.BooleanField(default=False),
        ),
    ]
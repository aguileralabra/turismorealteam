# Generated by Django 3.1.2 on 2020-10-25 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_auto_20201025_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='servicioextra',
            field=models.ManyToManyField(blank=True, null=True, to='aplicacion.ServicioExtra'),
        ),
    ]

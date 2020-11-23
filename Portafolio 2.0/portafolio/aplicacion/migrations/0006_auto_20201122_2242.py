# Generated by Django 3.1.2 on 2020-11-23 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0005_reserva_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='Imagen_Entorno',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='Imagen_Recinto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='check',
            field=models.CharField(choices=[('NoCheck', 'NoCheck'), ('CheckIn', 'CheckIn'), ('CheckOut', 'CheckOut')], default='No Check', max_length=100),
        ),
    ]

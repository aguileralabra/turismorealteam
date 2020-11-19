# Generated by Django 3.1.2 on 2020-11-19 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicioextra',
            name='transporte',
        ),
        migrations.AddField(
            model_name='servicioextra',
            name='conductor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.conductor'),
        ),
        migrations.DeleteModel(
            name='Transporte',
        ),
    ]

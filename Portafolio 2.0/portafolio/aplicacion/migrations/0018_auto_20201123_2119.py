# Generated by Django 3.1.2 on 2020-11-24 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0017_auto_20201123_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='Disponible',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], default='Si', max_length=2),
        ),
    ]

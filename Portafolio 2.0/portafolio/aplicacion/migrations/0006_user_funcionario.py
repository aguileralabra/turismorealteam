# Generated by Django 3.1.2 on 2020-11-11 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0005_auto_20201110_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='funcionario',
            field=models.BooleanField(default=False),
        ),
    ]

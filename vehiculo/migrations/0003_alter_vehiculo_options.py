# Generated by Django 4.0.5 on 2023-07-11 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_vehiculo_condicion_precio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'permissions': (('visualizar_catalogo', 'Visualizar Catalogo'),)},
        ),
    ]

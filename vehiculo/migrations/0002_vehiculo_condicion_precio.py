# Generated by Django 4.0.5 on 2023-07-10 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='condicion_precio',
            field=models.CharField(choices=[('Bajo', 'Bajo'), ('Medio', 'Medio'), ('Alto', 'Alto')], default='Bajo', max_length=20),
        ),
    ]

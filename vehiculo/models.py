from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    MARCA_CHOICES = (
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    )

    CATEGORIA_CHOICES = (
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    )

    CONDICION_CHOICES = (
        ('Bajo', 'Bajo'),
        ('Medio', 'Medio'),
        ('Alto', 'Alto'),
    )

    marca = models.CharField(max_length=20, choices=MARCA_CHOICES, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='Particular')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    condicion_precio = models.CharField(max_length=20, choices=CONDICION_CHOICES, default='Bajo')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')


    def __str__(self):
        return f"{self.marca} {self.modelo} {self.serial_carroceria} {self.serial_motor} {self.categoria} {self.precio} {self.condicion_precio}"

    class Meta:
        permissions = (
            ('visualizar_catalogo', 'Visualizar Catalogo'),
        )
    

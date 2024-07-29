from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    fecha_donacion = models.DateField()
    CONDICION_CHOICES = [
        ('mala', 'Mala'),
        ('buena', 'Buena'),
        ('excelente', 'Excelente'),
    ]
    condicion = models.CharField(max_length=10, choices=CONDICION_CHOICES)
    nombre_donante = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

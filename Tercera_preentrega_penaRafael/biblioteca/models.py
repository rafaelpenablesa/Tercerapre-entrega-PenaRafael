from django.db import models
from django.contrib.auth.models import User

class Prestatario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

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

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    prestatario = models.ForeignKey(Prestatario, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.libro.titulo} prestado a {self.prestatario.nombre}"


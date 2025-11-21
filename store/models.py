from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.EmailField()
    telefono = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nombre

class Cancion(models.Model):
    titulo = models.CharField(max_length=255)
    artista = models.CharField(max_length=255)
    año = models.PositiveIntegerField()
    duracion_seg = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.titulo} - {self.artista}"

class Vinilo(models.Model):
    titulo = models.CharField(max_length=255)
    artista = models.CharField(max_length=255)
    año = models.PositiveIntegerField()
    canciones = models.ManyToManyField(Cancion, blank=True)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo

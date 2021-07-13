from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import CASCADE

# Create your models here.

class Residente(models.Model):
    id = models.IntegerField(primary_key=True)
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    fechaNacimiento = models.DateField()
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido
    

class Paramedico(models.Model):
    id = models.IntegerField(primary_key=True)
    nombreP = models.CharField(max_length=100)
    rutP = models.CharField(max_length=10, null=True)
    fechaNacP = models.DateField(null=True)

    def __str__(self):
        return self.nombreP


class Pieza(models.Model):
    id = models.IntegerField(primary_key=True)
    nroPieza = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)])
    estado = models.BooleanField(default=True)
    residente = models.ForeignKey(Residente, blank=True, null=True, on_delete=models.CASCADE)
    paramedico = models.ForeignKey(Paramedico, blank=True, null=True, on_delete=models.CASCADE) 
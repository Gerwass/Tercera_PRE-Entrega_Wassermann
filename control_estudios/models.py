from django.db import models

# Create your models here.
class Curso (models.Model):
    #los atributos de clase(son las columnas de la tabla)
    nombre = models.CharField(max_length=64)
    comision = models.IntegerField()

    def __str__(self):
        return f"{self.nombre},{self.comision}"


class Estudiante(models.Model):
    apellido=models.CharField(max_length=256)
    nombre=models.CharField(max_length=256)
    email=models.EmailField(blank=True)
    telefono=models.CharField(max_length=20,blank=True)
    dni=models.CharField(max_length=32)
    fecha_nacimiento=models.DateField(null=True)

    def __str__(self):
        return f"{self.apellido},{self.nombre}"

class Profesor(models.Model):
    apellido=models.CharField(max_length=256)
    nombre=models.CharField(max_length=256)
    email=models.EmailField(blank=True)
    telefono=models.CharField(max_length=20,blank=True)
    dni=models.CharField(max_length=32)
    fecha_nacimiento=models.DateField(null=True)
    profesion=models.CharField(max_length=128)
    def __str__(self):
        return f"{self.apellido},{self.nombre}"


class Entregable(models.Model):
    pass
    #nombre=
    #fecha_entrega=
    #esta_aprobado=

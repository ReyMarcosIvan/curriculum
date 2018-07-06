from django.db import models
from django.utils import timezone



class Estudio(models.Model):
    author = models.ForeignKey('auth.User')
    carrera= models.CharField(max_length=200)
    lugar= models.CharField(max_length=200)
    sede= models.CharField(max_length=200)
    comienzo = models.CharField(max_length=200)
    fin = models.CharField(max_length=200)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return ""

class Experiencia(models.Model):
    author = models.ForeignKey('auth.User')
    trabajo= models.CharField(max_length=200)
    descripcion=models.TextField()
    lugar= models.CharField(max_length=200)
    comienzo = models.CharField(max_length=200)
    fin = models.CharField(max_length=200)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return ""

class Lenguajes(models.Model):
    author = models.ForeignKey('auth.User')
    nombre= models.CharField(max_length=200)

    def __str__(self):
        return ""

from django.db import models
from django.db.models.fields import DateTimeField
from django.contrib.auth.models import User

class Estados(models.TextChoices):
    CREADA = 'Creada'
    INICIADA = 'Iniciada'
    SUSPENDIDA = 'Suspendida'
    FINALIZADA = 'Finalizada'
    INCOMPLETA = 'Incompleta'

class Tarea(models.Model):
    
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.CharField(choices=Estados.choices, max_length=10)   
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)  
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


    class Meta:

        verbose_name= "tarea"
        verbose_name_plural="tareas"    

    def __str__(self):
        return f'{self.titulo} '
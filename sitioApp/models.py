from django.db import models

# Create your models here.
class Descarga(models.Model):
    id= models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100,verbose_name="Descripción")
    tamaño = models.CharField(max_length=100,verbose_name="Tamaño")
    descarga = models.FileField(blank=True, null=True)

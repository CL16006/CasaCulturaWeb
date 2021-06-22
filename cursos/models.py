from django.db import models
from django.forms import ModelForm

#Aqui estan definidos todos los modelos

#Modelo para la tabla cursos
class cursos(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()

    def __str__(self):
        return self.nombre

#Modelo para la tabla inscripcion
class inscripcion(models.Model):
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.IntegerField()
    curso=models.ForeignKey(cursos, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombres

#Modelo para la tabla anuncio
class anuncio(models.Model):
    fecha_publicacion=models.DateTimeField()
    encabezado=models.CharField(max_length=200)
    imagen=models.ImageField(upload_to='images/',null=True, blank=True)
    texto=models.TextField()

    def __str__(self):
        return self.encabezado
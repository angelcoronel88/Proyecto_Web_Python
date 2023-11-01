from django.db import models

# Create your models here.
class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Editores'

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Autores'


class Libro(models.Model):
    titulo = models.CharField(max_length=25)
    autor = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
    def nombre_y_apellido(self):
        return ','.join([Autor.nombre for Autor in self.autor.all()]+[Autor.apellido for Autor in self.autor.all()])

    class Meta:
        ordering = ['titulo']
        verbose_name_plural = 'Libros'


    
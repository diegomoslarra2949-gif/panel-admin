from django.db import models


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateField(verbose_name="Fecha del suceso")
    lugar = models.CharField(max_length=150)
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(upload_to="noticias/")

    class Meta:
        ordering = ["-fecha"]
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __str__(self):
        return self.titulo
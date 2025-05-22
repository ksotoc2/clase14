from django.db import models
from django.contrib.auth.models import User

# Modelo de Libro
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

# Modelo de Reseña
class Resenia(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='resenias')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    puntuacion = models.PositiveIntegerField(default=3)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.libro.titulo} - {self.autor.username}"

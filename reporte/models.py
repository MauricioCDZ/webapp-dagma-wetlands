from django.db import models
from django.utils import timezone
from django.conf import settings

from django.urls import reverse

#from django.contrib.auth.models import User
User = settings.AUTH_USER_MODEL
# Create your models here.
class Reporte(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_reporte = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='reporte_pics')

    HUMEDALES = (
        ('1', 'La Babilla'),
        ('2', 'El Retiro'),
        ('3', 'Ecoparque Las Garzas'),
    )
    humedal = models.CharField(max_length=1, choices=HUMEDALES)

    def __str__(self):
        return self.titulo
    

    def get_absolute_url(self):
        return reverse('reporte-detail', kwargs={'pk': self.pk})
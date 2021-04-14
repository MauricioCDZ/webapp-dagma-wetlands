from django.db import models
from django.utils import timezone
from django.conf import settings

from django.urls import reverse

#from django.contrib.auth.models import User
User = settings.AUTH_USER_MODEL
# Create your models here.
import os, io
from google.cloud import vision_v1
from PIL import Image
from google.cloud.vision_v1 import types
from captcha.fields import ReCaptchaField

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/mauricio/Documentos/graduation_project/reporte/humedales-cali-token.json'
client = vision_v1.ImageAnnotatorClient()


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

    def save(self, *args, **kwargs):
        #super().save()

        #img = Image.open(self.image)

        content = self.image.read()
        image = vision_v1.types.Image(content=content)
        response = client.safe_search_detection(image=image)
        safe_search = response.safe_search_annotation

        likelihood = ('Unknown', 'Very Unlikely', 'Unlikely','Possible', 'Likely', 'Very Likely')

        likelihood1 = (
			'Possible', 'Likely', 'Very Likely')

        if (likelihood[safe_search.adult] in  likelihood1  or likelihood[safe_search.medical] in  likelihood1 or likelihood[safe_search.violence] in  likelihood1 or likelihood[safe_search.racy] in  likelihood1):
            self.titulo = "Contenido Bloqueado"
            self.image = 'media/default.jpg'
            self.descripcion = "Contenido Bloqueado por imagen posiblemente explicita."
        #self.titulo=self.image.path
        """
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path) """

        super(Reporte, self).save(*args, **kwargs)
            

# Create your models here.
class Comuna(models.Model):
	nombre = models.CharField(max_length= 200, null=False)
	def __str__(self):
		return self.nombre
class TipoHumedal(models.Model):
	nombre = models.CharField(max_length= 200, null=False)
	numAsignado = models.IntegerField(null=False)
	def __str__(self):
		return self.nombre

class Usuario(models.Model):
	nombre = models.CharField(max_length= 200, null=False)
	celular = models.IntegerField(null=False)
	correoElectronico = models.EmailField(max_length= 200, null=False)
	password = models.CharField(max_length= 200, null=False)
	cedula = models.IntegerField(null=False)
	def __str__(self):
		return self.nombre
def validate_image(image):
	file_size = image.file.size
	limit_mb = 10
	if file_size > limit_mb * 1024 * 1024:
		raise ValidationError("Max size of file is %s MB" % limit_mb)
class TipoAporte(models.Model):
	nombre = models.CharField(max_length= 200, null=False)
	def __str__(self):
		return self.nombre
class Aporte(models.Model):
	nombreHumedal = models.ForeignKey('Humedales', on_delete=models.CASCADE, null=False)
	nombreUsuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=False)
	tipoAporte = models.ForeignKey('TipoAporte', on_delete=models.CASCADE, null=False)
	imagen = models.ImageField('Image', upload_to='uploads/', validators=[validate_image], null=True, blank=True)
	descripcion = models.TextField(null=False)
	STATUS = (('Visible', 'Visible'), ('Invisible', 'Invisible'))
	IMPORTANCIA = (('Muy Importante', 'Muy Importante'), ('Regular', 'Regular'))
	status = models.CharField(max_length= 200, null=False, choices=STATUS)
	importancia = models.CharField(max_length= 200, null=False, choices=IMPORTANCIA)
class Humedales(models.Model):
	nombre = models.CharField(max_length= 200, null=False)
	areaEstacional = models.FloatField(null=False)
	areaPermanente = models.FloatField(null=False)
	latitud = models.FloatField(null=False)
	altitud = models.FloatField(null=False)
	jurisdiccion = models.ForeignKey('Comuna', on_delete=models.CASCADE, null=False)
	tipoHumedal= models.ForeignKey('TipoHumedal', on_delete=models.CASCADE, null=False)
	dateCreated = models.DateTimeField(auto_now_add= True, null=False)
	def __str__(self):
		return self.nombre
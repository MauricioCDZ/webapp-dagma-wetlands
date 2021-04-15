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
#from captcha.fields import ReCaptchaField

#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/mauricio/Documentos/graduation_project/reporte/humedales-cali-token.json'
#client = vision_v1.ImageAnnotatorClient()


def validate_image(image):
	file_size = image.file.size
	limit_mb = 10
	if file_size > limit_mb * 1024 * 1024:
		raise ValidationError("Max size of file is %s MB" % limit_mb)
class Reporte(models.Model):
    nombreUsuario = models.ForeignKey(User,on_delete=models.CASCADE, null=False)
    nombreHumedal = models.ForeignKey('Humedal', on_delete=models.CASCADE, null=False)
    titulo = models.CharField(max_length= 100, null=False)
    descripcion = models.TextField(null=False)
    fecha_reporte = models.DateTimeField(default=timezone.now, null=False)
    #fecha_reporte = models.DateTimeField(auto_now_add= True, null=False)
    image = models.ImageField(upload_to='reporte_pics', validators=[validate_image], null=False)
    tipoReporte = models.ForeignKey('TipoReporte', on_delete=models.CASCADE, null=False)
    STATUS = (('Visible', 'Visible'), ('Invisible', 'Invisible'))
    IMPORTANCIA = (('Muy Importante', 'Muy Importante'), ('Regular', 'Regular'))
    status = models.CharField(max_length= 200, null=False, choices=STATUS)
    importancia = models.CharField(max_length= 200, null=False, choices=IMPORTANCIA)

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
	numero = models.IntegerField(null=False)
	dateCreated = models.DateTimeField(auto_now_add= True, null=False)
	def __str__(self):
		return str(self.numero)
class TipoHumedal(models.Model):
	nombre = models.CharField(max_length= 200, null=False)
	numAsignado = models.IntegerField(null=False)
	dateCreated = models.DateTimeField(auto_now_add= True, null=False)
	def __str__(self):
		return self.nombre

class TipoReporte(models.Model):
	nombre = models.CharField(max_length= 200, null=False)
	dateCreated = models.DateTimeField(auto_now_add= True, null=False)
	def __str__(self):
		return self.nombre
class Flora(models.Model):
	nombre = models.CharField(max_length= 200, null=False)
	familia = models.ForeignKey('FamiliaFlora', on_delete=models.CASCADE, null=False)
	foto =  models.ImageField('Image', upload_to='flora/', null=False)
	dateCreated = models.DateTimeField(auto_now_add= True, null=False)
	def __str__(self):
		return self.nombre 
class FamiliaFlora(models.Model):
	nombre = models.CharField(max_length= 200, null=False)
	dateCreated = models.DateTimeField(auto_now_add= True, null=False)
	def __str__(self):
		return self.nombre 
class FaunaTerrestre(models.Model):
	nombre = models.CharField(max_length= 200, null=False)
	familia = models.ForeignKey('FamiliaFauna', on_delete=models.CASCADE, null=False)
	foto =  models.ImageField('Image', upload_to='faunaTerrestre/', null=False)
	dateCreated = models.DateTimeField(auto_now_add= True, null=False)
	def __str__(self):
		return self.nombre 
class FamiliaFauna(models.Model):
	nombre = models.CharField(max_length= 200, null=False)
	dateCreated = models.DateTimeField(auto_now_add= True, null=False)
	def __str__(self):
		return self.nombre
class FaunaAcuatica(models.Model):
	nombre = models.CharField(max_length= 200, null=False)
	familia = models.ForeignKey('FamiliaFauna', on_delete=models.CASCADE, null=False)
	foto =  models.ImageField('Image', upload_to='faunaAcuatica/', null=False)
	dateCreated = models.DateTimeField(auto_now_add= True, null=False)
	def __str__(self):
		return self.nombre 
class FloraHumedal(models.Model):
	nombreHumedal = models.ForeignKey('Humedal', on_delete=models.CASCADE, null=False)
	nombreFlora = models.ForeignKey('Flora', on_delete=models.CASCADE, null=False)
	dateCreated = models.DateTimeField(auto_now_add= True, null=False)
class FaunaTerrestreHumedal(models.Model):
	nombreHumedal = models.ForeignKey('Humedal', on_delete=models.CASCADE, null=False)
	nombreFauna = models.ForeignKey('FaunaTerrestre', on_delete=models.CASCADE, null=False)
	dateCreated = models.DateTimeField(auto_now_add= True, null=False)
class FaunaAcuaticaHumedal(models.Model):
	nombreHumedal = models.ForeignKey('Humedal', on_delete=models.CASCADE, null=False)
	nombreFaunaAcuatica = models.ForeignKey('FaunaAcuatica', on_delete=models.CASCADE, null=False)
	dateCreated = models.DateTimeField(auto_now_add= True, null=False)
class Humedal(models.Model):
	nombre = models.CharField(max_length= 200, null=False)
	areaEstacional = models.FloatField(null=False)
	areaPermanente = models.FloatField(null=False)
	latitud = models.FloatField(null=False)
	altitud = models.FloatField(null=False)
	jurisdiccion = models.ForeignKey('Comuna', on_delete=models.CASCADE, null=False)
	tipoHumedal= models.ForeignKey('TipoHumedal', on_delete=models.CASCADE, null=False)
	dateCreated = models.DateTimeField(auto_now_add= True, null=False)
	faunaTerrestre = models.ManyToManyField(FaunaTerrestre, through = 'FaunaTerrestreHumedal')
	FaunaAcuatica = models.ManyToManyField(FaunaAcuatica, through = 'FaunaAcuaticaHumedal')
	flora = models.ManyToManyField(Flora, through = 'FloraHumedal')
	def __str__(self):
		return self.nombre
class InvolucrateMensaje(models.Model):
	nombre = models.CharField(max_length= 200, null=False)
	correoElectronico = models.EmailField(max_length= 200, null=False)
	asunto = models.CharField(max_length= 200, null=False)
	descripcion = models.TextField(null=False)
	def __str__(self):
		return self.asunto 
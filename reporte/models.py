from django.db import models

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

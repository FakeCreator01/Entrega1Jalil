from django.db import models

# Create your models here.
class Bebe(models.Model):
	nombre = models.CharField(max_length=100)
	edad = models.IntegerField(verbose_name='edad (meses)') # sólo meses
	vacunado = models.BooleanField(default=False)

	def __str__(self):
		return self.nombre


class Comida(models.Model):
	nombre = models.CharField(max_length=150)
	cantidad = models.IntegerField(verbose_name='cantidad (gramos por bebe)') # + kgs

	def __str__(self):
		return self.nombre

		

class Niniera(models.Model):
	nombre = models.CharField(max_length=150)
	edad = models.IntegerField()
	años_experiencia = models.IntegerField()

	def __str__(self):
		return self.nombre

		
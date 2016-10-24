from . import models
from django.forms import ModelForm

class ArchivoForm(ModelForm):
	class Meta:
		model = models.Archivo
		fields = ['titulo', 'descripcion', 'upload', 'url']
	
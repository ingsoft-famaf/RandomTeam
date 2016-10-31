from . import models
from django.forms import ModelForm, HiddenInput

class ArchivoForm(ModelForm):
	class Meta:
		model = models.Archivo
		fields = ['titulo', 'descripcion', 'upload', 'url', 'goal', 'owner']
		widgets = {'goal': HiddenInput(), 'owner': HiddenInput() }
	
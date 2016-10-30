from . import models
from django.forms import ModelForm, HiddenInput

class ArchivoForm(ModelForm):
	class Meta:
		model = models.Archivo
		fields = ['titulo', 'descripcion', 'upload', 'url', 'goal', 'is_public', 'owner']
		widgets = {'goal': HiddenInput(),'is_public': HiddenInput(), 'owner': HiddenInput()}  
				   
	
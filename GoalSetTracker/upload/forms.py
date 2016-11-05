from . import models
from django.forms import ModelForm, HiddenInput, FileInput
from django import forms


class ArchivoForm(ModelForm):
	upload = forms.FileField(label=('upload'), required=False, widget=forms.FileInput)
	class Meta:
		model = models.Archivo
		fields = ['titulo', 'descripcion', 'upload', 'url', 'goal', 'owner']
		widgets = {'goal': HiddenInput(), 'owner': HiddenInput()}
	
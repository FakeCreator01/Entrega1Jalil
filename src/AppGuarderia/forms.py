from django import forms
from django.forms import ModelForm
from .models import Bebe, Niniera, Comida


class BebeForm(ModelForm):
	class Meta:
		model = Bebe
		fields = ('__all__')


class NinieraForm(ModelForm):
	class Meta:
		model = Niniera
		fields = ('__all__')


class ComidaForm(ModelForm):
	class Meta:
		model = Comida
		fields = ('__all__')





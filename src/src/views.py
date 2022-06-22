from django.shortcuts import render
from AppGuarderia.models import Niniera, Comida

def inicio(request):

	ninieras = Niniera.objects.all()
	comidas = Comida.objects.all()

	return render(request, 'inicio.html', {
		'ninieras': ninieras,
		'comidas': comidas,
		})
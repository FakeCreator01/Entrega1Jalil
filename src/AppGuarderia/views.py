from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bebe, Niniera, Comida
from .forms import BebeForm, NinieraForm, ComidaForm

# Create your views here.

def buscar(request):

	if request.GET['nombre_bebe']:

		respuesta = f"Resultados para bebes cuyo nombre es {request.GET['nombre_bebe']}."

		nombre_bebe = request.GET['nombre_bebe']

		bebes = Bebe.objects.filter(nombre__icontains=nombre_bebe)
		
		if bebes.count() == 0:
			print("coca")
			respuesta = 'No se encontraron bebes con ese nombre.'

		return render(request, 'inicio.html', {
			'nombre_bebe': nombre_bebe,
			'bebes':bebes,
			'respuesta': respuesta,
			})

	else:
		respuesta = "No enviaste datos." # crear template basico "no enviaste datos, volver"

	return render(request, 'inicio.html', {
		'respuesta': respuesta,
		})


def bebe(request):

	lista_bebes = Bebe.objects.all()
	form = BebeForm
	mi_formulario = BebeForm(request.POST)

	# Devuelve template con la lista de bebes

	if request.method == 'POST' and mi_formulario.is_valid():

		mi_formulario.save()

		return redirect('inicio')

	return render(request, 'AppGuarderia/bebes.html', {
		'form': form,
		})


def niniera(request):

	lista_ninieras = Niniera.objects.all()
	form = NinieraForm
	mi_formulario = NinieraForm(request.POST)

	# Devuelve template con la lista de niñeras

	if request.method == 'POST' and mi_formulario.is_valid():

		mi_formulario.save()

		return redirect('inicio')

	return render(request, 'AppGuarderia/ninieras.html', {
		'form': form,
		})


def comida(request):

	lista_comidas = Comida.objects.all()
	form = ComidaForm
	mi_formulario = ComidaForm(request.POST)

	# Devuelve template con la lista de comidas

	if request.method == 'POST' and mi_formulario.is_valid():

		mi_formulario.save()

		return redirect('inicio')

	return render(request, 'AppGuarderia/comidas.html', {
		'form': form,
		})
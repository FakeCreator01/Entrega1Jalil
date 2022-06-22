from django.urls import path
from .views import bebe, niniera, comida, buscar

app_name = 'AppGuarderia'

urlpatterns = [
	
	path('bebes/', bebe, name="bebes"),
	path('ninieras/', niniera, name="ninieras"),
	path('comidas/', comida, name="comidas"),
	path('buscar/', buscar, name="buscar"),
	
]
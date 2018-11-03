from django.urls import path 
from .views import *

urlpatterns = [
	path('login/',vista_login),
	path('conexion/',postsign,name='inicio'),
	path('logout/',logout,name='logout'),
	path('registro/',registro,name='registro'),
	path('registrar/',registrar,name='registrar'),
	path('registro_comida/',vista_registro_comida, name='vista_registro_comida'),
	path('lista_comida/',vista_lista_comida, name='vista_lista_comida'),
	path('agregar_deporte/',vista_agregar_deporte,name='agregar_deporte'),
	path('listar_deporte/',vista_listar_deporte,name='listar_deporte'),
	path('lista_perfil/',lista_perfil, name='lista_perfil'),

]
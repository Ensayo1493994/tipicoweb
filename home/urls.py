from django.urls import path 
from .views import *

urlpatterns = [
	path('login/',vista_login, name='vista_login'),
	path('conexion/',postsign,name='postsign'),
	path('login/',vista_login),
	path('conexion/',postsign,name='login'),
	path('logout/',logout,name='logout'),
	path('registro/',registro,name='registro'),
	path('registrar/',registrar,name='registrar'),
	path('registro_comida/',vista_registro_comida, name='vista_registro_comida'),
	path('lista_comida/',vista_lista_comida, name='vista_lista_comida'),
	path('agregar_deporte/',vista_agregar_deporte,name='agregar_deporte'),
	path('listar_deporte/',vista_listar_deporte,name='listar_deporte'),
	path('editar_deporte/<int:iden>',vista_editar_deporte,name='editar_deporte'),
	path('editar_perfil/<int:idenu>',vista_editar_perfil,name='editar_perfil'),
	path('editar_perfil/',vista_editar_perfil,name='ver_editar_perfil'),
	path('lista_perfil/',lista_perfil, name='lista_perfil'),
	path('inicio/',inicio, name='inicio'),


]
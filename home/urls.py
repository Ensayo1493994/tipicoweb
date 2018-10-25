from django.urls import path 
from .views import *

urlpatterns = [
	path('login/',vista_login),
	path('conexion/',postsign),
	path('logout/',logout,name='logout'),
	path('registro/',registro,name='registro'),
	path('registrar/',registrar,name='registrar'),
]
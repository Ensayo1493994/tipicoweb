from django.shortcuts import render
import pyrebase
from django.contrib import auth
import traceback

# Create your views here.

'''CONFIGURACION DE FIREBASE EN LA WEB'''
config = {
    'apiKey': "AIzaSyD4rA3-ZMXJkiQwJdhQeFmYMicCe1pyfPc",
    'authDomain': "tipico-saludable-50fb7.firebaseapp.com",
    'databaseURL': "https://tipico-saludable-50fb7.firebaseio.com",
    'projectId': "tipico-saludable-50fb7",
    'storageBucket': "tipico-saludable-50fb7.appspot.com",
    'messagingSenderId': "159019297528"
  }
'''INICIALIZACION DE LA APP'''
firebase = pyrebase.initialize_app(config)
database = firebase.database()


'''AUTENTICCION EN FIREBASE DEL USUARIO'''
authe = firebase.auth()


'''VISTA INICIAR SESION'''
def vista_login(request):
 	
	return render(request,'login.html')
	
'''FUNCION DE AUTENTICACION EN FIREBASE'''
def postsign(request):
	email = request.POST.get('email')
	passw = request.POST.get('password')
	try:
		user = authe.sign_in_with_email_and_password(email, passw)
	except:
		message="CONTRASEÑA O USUARIO INCORRECTO"
		return render(request,'login.html',{'mensaje':message})
	print(user['idToken'])
	session_id = user['idToken']
	request.session['uid']=str(session_id)
	return render(request,'index.html',{'e':email})

def logout(request):
	auth.logout(request)
	return render(request,'login.html')

'''FUNCION DE REGISTRO DE PERFIL EN FIREBASE'''
def registro(request):
	return render(request,'registro.html')

def registrar(request):

	email = request.POST.get('email')
	passw = request.POST.get('password')
	print(email)
	try:
		user = authe.create_user_with_email_and_password(email,passw)
		data={
			"correo":email
		}
		database.child("Usuarios").push(data)
	except:
		mensaje="No se puede crear la cuenta"
		print('oscar',passw)
		return render(request,'registro.html',{'mensaje':mensaje},{'dato':email})
		uid = user['localId']

	
	return render(request,'registro.html')

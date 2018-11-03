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
	nombre = request.POST.get('nombre')
	foto = request.POST.get('foto')
	rol = request.POST.get('rol') 
	#sizeList =0
	#all_users = database.get()
	#for Usuarios in 

	#.each():
		#sizeList=sizeList+1

	print(email,passw,nombre,rol)
	try:
		#user = authe.create_user_with_email_and_password(email,passw)
		#print(user)
		data={
			"correo":email,
			"contraseña":passw,
			"nombre":nombre,
			"foto":foto,
			"rol":rol
		}
		database.child("Usuarios").child(""+sizeList).set(data)
	except:
		mensaje="No se puede crear la cuenta"
		return render(request,'registro.html',{'mensaje':mensaje},{'dato':email})
		uid = user['localId']

	
	return render(request,'registro.html')

def vista_registro_comida(request):
	nombre = request.POST.get('nombre')
	calorias = request.POST.get('calorias')
	carbohidratos = request.POST.get('carbohidratos')
	proteinas = request.POST.get('proteinas')
	imagen = request.POST.get('imagen')
	receta = request.POST.get('receta')
	print(nombre,calorias,proteinas,imagen)
	try:
		#user = authe.create_user_with_email_and_password(email,passw)
		data= { 
				"nombre":nombre,
				"calorias":calorias,
				"carbohidratos":carbohidratos,
				"proteinas":proteinas,
				"imagen":imagen,
				"receta":receta,
		}
		database.child("Comida").push(data)	
	except:
		mensaje="No se puede guardar los datos"
		return render(request, 'registro_comida.html',{'mensaje':mensaje},{'db': nombre})
		uid = nombre['localId']
	
	return render(request, 'registro_comida.html')

def vista_lista_comida(request):
	timestamps = database.child("Comida").shallow().get().val()
	list_time=[]
	for i in timestamps:
		list_time.append(i)
	list_time.sort(reverse=True)
	print(list_time)

	nom=[]
	for i in list_time:
		nombre = database.child("Comida").child(i).child("Nombre").get().val()
		nom.append(nombre)
	print(nom)

	calor=[]
	for i in list_time:
		calorias = database.child("Comida").child(i).child("Calorias").get().val()
		calor.append(calorias)
	print(calor)

	carbo=[]
	for i in list_time:
		carbohidratos = database.child("Comida").child(i).child("Carbohidratos").get().val()
		carbo.append(carbohidratos)
	print(carbo)

	prot=[]
	for i in list_time:
		proteinas = database.child("Comida").child(i).child("Proteinas").get().val()
		prot.append(proteinas)
	print(prot)

	paquete_list = zip(nom,calor,carbo,prot)

	return render(request, 'lista_comida.html', locals())






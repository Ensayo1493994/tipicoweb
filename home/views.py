from django.shortcuts import render
import pyrebase
from django.contrib import auth
import traceback
import pytz

# Create your views here.

valor=0
comida=0
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
storage = firebase.storage()



'''AUTENTICCION EN FIREBASE DEL USUARIO'''
authe = firebase.auth()

def inicio(request):
 	
	return render(request,'index.html')
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

	return render(request,'plantillaBase.html',{'e':email})

def logout(request):
	auth.logout(request)
	return render(request,'login.html')

	
'''FUNCION DE REGISTRO DE PERFIL EN FIREBASE'''
def registro(request):
	return render(request,'registro.html')

def registrar(request):

	try:
		#el child en el cual se va a agregar es Usuario
		timestamps= database.child("Usuarios").shallow().get().val()
		lis_time=[]
		for i in timestamps:

			lis_time.append(i)
		
		lis_time.sort(reverse=False)
		print(lis_time)
		valor=len(lis_time)

		ultimo_elemento=lis_time[valor-1]
		print("ultimo elemnto: ",ultimo_elemento)
		siguiente_elemento=(int(ultimo_elemento)+1)
		print("siguiente elemnto: ",siguiente_elemento)
		#obtienen el tamaño de la lista
		print("valor: ",valor)

	except:
		print("Hay algo raro")

	email = request.POST.get('email')
	passw = request.POST.get('password')
	nombre = request.POST.get('nombre')
	iddrawable= request.POST.get('url')
	rol = request.POST.get('rol') 
	print(email,passw,nombre,iddrawable,rol)

	try:

		timestamps2= database.child("Usuarios").shallow().get().val()
		lis_time2=[]
		for i in timestamps2:

			lis_time2.append(i)
		
		lis_time.sort(reverse=False)
		print(lis_time2)
		valor2=len(lis_time2)
		#obtienen el tamaño de la lista
		print("valor 2: ",valor2)
		#user = authe.create_user_with_email_and_password(email,passw)
		if(valor==valor2):
			print("valor final: ",valor)
			data={
				"correo":email,
				"contraseña":passw,
				"nombre":nombre,
				"idDrawable":iddrawable,
				"rol":rol
			}
		database.child("Usuarios").child(str(siguiente_elemento)).set(data)

	except:
		mensaje="No se puede crear la cuenta"
		return render(request,'registro.html',{'mensaje':mensaje})
		#uid = user['localId']

	return render(request,'registro.html')

def lista_perfil(request):
	timestamps = database.child("Usuarios").shallow().get().val()
	lista_time=[]
	for i in timestamps:
		lista_time.append(i)
	lista_time.sort(reverse=True)
	print(lista_time)

	nom=[]
	for i in lista_time:
		nombre = database.child("Usuarios").child(i).child("nombre").get().val()
		nom.append(nombre)
	print(nom)

	role=[]
	for i in lista_time:
		rol = database.child("Usuarios").child(i).child("rol").get().val()
		role.append(rol)
	print(rol)

	foto=[]
	for i in lista_time:
		imagencomida = database.child("Usuarios").child(i).child("idDrawable").get().val()
		foto.append(imagencomida)
	print(foto)

	correou=[]
	for i in lista_time:
		correo = database.child("Usuarios").child(i).child("correo").get().val()
		correou.append(correo)
	print(correo)

	paquete_list = zip(lista_time,nom,role,foto,correou)

	return render(request, 'perfiles.html', locals())

#REGISTRO COMIDAS

def vista_registro_comida(request):
	#primero se lista los datos del nodo
	try:
		#el child en le cual se va a agregar es Deporte
		timestamps= database.child("Comida").shallow().get().val()
		lista_time=[]
		for i in timestamps:

			lista_time.append(i)
		
		lista_time.sort(reverse=True)
		print(lista_time)
		valor=len(lista_time)
		#obtienen el tamaño de la lista
		print("comida: ",comida)

	except:
		pass
		print("problemas")
	nombre = request.POST.get('nombre')
	calorias = request.POST.get('calorias')
	carbohidratos = request.POST.get('carbohidratos')
	proteinas = request.POST.get('proteinas')
	iddrawable= request.POST.get('url')
	receta = request.POST.get('url')
	print(nombre,calorias,proteinas,iddrawable)

	
	try:
		timestamps3= database.child("Comida").shallow().get().val()
		lista_time3=[]
		for i in timestamps3:

			lista_time3.append(i)
		
		lista_time.sort(reverse=True)
		print(lista_time3)
		comida2=len(lista_time3)
		#obtienen el tamaño de la lista
		print("comida 2: ",comida2)
		#user = authe.create_user_with_email_and_password(email,passw)

		if(comida==comida2):
			print("valor final: ",comida)
		#user = authe.create_user_with_email_and_password(email,passw)
		data= { 
				"Nombre":nombre,
				"Calorias":calorias,
				"Carbohidratos":carbohidratos,
				"Proteinas":proteinas,
				"Receta":receta,
				"idDrawable":iddrawable,
		}
		database.child("Comida").child(str(valor)).set(data)	
	except:
		mensaje="No se puede guardar los datos"
		return render(request, 'registro_comida.html',{'mensaje':mensaje},{'db': nombre})
		uid = nombre['localId']
	
	return render(request, 'registro_comida.html')

def vista_lista_comida(request):
	timestamps = database.child("Comida").shallow().get().val()
	lista_time=[]
	for i in timestamps:
		lista_time.append(i)
	lista_time.sort(reverse=True)
	print(lista_time)

	nom=[]
	for i in lista_time:
		nombre = database.child("Comida").child(i).child("Nombre").get().val()
		nom.append(nombre)
	print(nom)

	calor=[]
	for i in lista_time:
		calorias = database.child("Comida").child(i).child("Calorias").get().val()
		calor.append(calorias)
	print(calor)

	carbo=[]
	for i in lista_time:
		carbohidratos = database.child("Comida").child(i).child("Carbohidratos").get().val()
		carbo.append(carbohidratos)
	print(carbo)

	prot=[]
	for i in lista_time:
		proteinas = database.child("Comida").child(i).child("Proteinas").get().val()
		prot.append(proteinas)
	print(prot)

	foto=[]
	for i in lista_time:
		imagencomida = database.child("Comida").child(i).child("idDrawable").get().val()
		foto.append(imagencomida)
	print(foto)

	paquete_list = zip(lista_time,foto,nom,calor,carbo,prot)

	return render(request, 'lista_comida.html', locals())

# logica de los deportes
def vista_agregar_deporte(request):

	lista= database.child("Deporte").shallow().get().val()
	lista_indices1=[]
	for i in lista:
		lista_indices1.append(i)
		
	lista_indices1.sort(reverse=False)
	print(lista_indices1)
	longitud=len(lista_indices1)
	#obtienen el tamaño de la lista
	print("longitud 1 : ",longitud)

	#primero se lista los datos del nodo
	try:
		#el child en le cual se va a agregar es Deporte
		lista= database.child("Deporte").shallow().get().val()
		lista_indices=[]
		for i in lista:

			lista_indices.append(i)
		
		lista_indices.sort(reverse=False)
		x = len(lista_indices)
		print("x: ",x)
		#print(x)
		ultimo_elemento = lista_indices[x-1]
		siguiente_elemento=(int(ultimo_elemento)+1)
		print("ultimo elemento de la lista: ",int(ultimo_elemento))
		print("siguiente elemto a crear: ",int(siguiente_elemento))
		#obtienen el tamaño de la lista
		# print("valor3: ",ultimo_elemento)

	except:
		print("Hay algo raro")


	nombre = request.POST.get('nombre')
	descripcion = request.POST.get('descripcion')
	calorias = request.POST.get('calorias')
	categoria = request.POST.get('categoria')
	duracion =request.POST.get('duracion')
	imagen= request.POST.get('url')
	# print(email)
	try:

		lista2= database.child("Deporte").shallow().get().val()
		lista_indices2=[]
		for i in lista2:

			lista_indices2.append(i)
		
		lista_indices2.sort(reverse=False)
		print(lista_indices2)
		longitud2=len(lista_indices2)
		#obtienen el tamaño de la lista
		print("longitud 2: ",longitud2)
		#user = authe.create_user_with_email_and_password(email,passw)

		if(longitud==longitud2):
			print("longitud final: ",longitud2)
			data={
				"nombre":nombre,
				"descripcion":descripcion,
				"calorias":calorias,
				"categoria":categoria,
				"duracion":duracion,
				"imagen":imagen
			}
		#se pasa el valor del tamaño de la lista a un chlid y se hace un set a dicho child
		database.child("Deporte").child(str(siguiente_elemento)).set(data)
		mensaje="Registro exitoso"
		
		return render(request,'agregar_deporte.html',{'mensaje':mensaje})
	except:
		mensaje="No se puede crear la cuenta"
		#print('oscar',passw)
		return render(request,'agregar_deporte.html',{'mensaje':mensaje})
		#uid = user['localId']

	
	return render(request,'agregar_deporte.html')

def vista_listar_deporte(request):
	# idtoken= request.session['uid']
	# a= authe.get_account_info(idtoken)
	# a=a['users']
	# a=a[0]
	# a=a['localid']

	timestamps= database.child("Deporte").shallow().get().val()
	lis_time=[]
	for i in timestamps:

		lis_time.append(i)
	
	lis_time.sort(reverse=True)
	print(lis_time)



	nombre=[]

	for i in lis_time:
		wor = database.child("Deporte").child(i).child("nombre").get().val()
		nombre.append(wor)
	print(nombre)



	cal=[]

	for a in lis_time:
		calorias=database.child("Deporte").child(a).child("calorias").get().val()
		cal.append(calorias)
	print(cal)



	des=[]

	for a in lis_time:
		descripcion=database.child("Deporte").child(a).child("descripcion").get().val()
		des.append(descripcion)
	print(des)


	cat=[]

	for a in lis_time:
		categoria=database.child("Deporte").child(a).child("categoria").get().val()
		cat.append(categoria)
	print(cat)


	dur=[]

	for a in lis_time:
		duracion=database.child("Deporte").child(a).child("duracion").get().val()
		dur.append(duracion)
	print(dur)



	ima=[]

	for a in lis_time:
		imagen=database.child("Deporte").child(a).child("imagen").get().val()
		ima.append(imagen)
	print(ima)




	comb_lis= zip(lis_time,nombre,cal,des,cat,dur,ima)



	return render(request,'listar_deporte.html',locals())





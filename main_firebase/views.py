from django.http import HttpResponseRedirect
from django.shortcuts import render
import main_firebase.models
import pyrebase
from django.db import connection
config={
  "apiKey": "AIzaSyAGlpseoXh8z8wVzomazZWn_24ILhymtWU",
  "authDomain": "biblioteca-s.firebaseapp.com",
  "databaseURL": "https://biblioteca-s-default-rtdb.firebaseio.com",
  "projectId": "biblioteca-s",
  "storageBucket": "biblioteca-s.appspot.com",
  "messagingSenderId": "174158602420",
  "appId": "1:174158602420:web:71cad95b89d480fec5f7e1",
  "measurementId": "G-PKZJMBSS5J"
}
#https://www.youtube.com/watch?v=bq0AszeDZf4
# Initialising database,auth and firebase for further use
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()
def signIn(request):
	return render(request,"main_firebase/Login.html")
def home(request ):
	#conteudo =SearchConteudos.objects.all()
	cursor = connection.cursor()
	cursor.execute("SELECT c.titulo, c.subtitulo, c.visibilidade, a.nome, a.sobrenome FROM conteudos c INNER JOIN autores a ON c.codigo_autor = a.codigo_autor;")
	conteudo = cursor.fetchall()	
	return render(request,"main_firebase/Home.html",{"conteudo": conteudo})
def Main(request):
	return render(request,"main_firebase/main.html")
       
def postsignIn(request):
	email=request.POST.get('email')
	pasw=request.POST.get('pass')
	try:
		user=authe.sign_in_with_email_and_password(email,pasw)
		#uid = user['localId']
		cursor = connection.cursor()
		cursor.execute("SELECT c.titulo, c.subtitulo, c.visibilidade, a.nome, a.sobrenome FROM conteudos c INNER JOIN autores a ON c.codigo_autor = a.codigo_autor;")
		conteudo = cursor.fetchall()	
	except:	
		message="Credenciais invalidas, verifique os dados de entrada"
	
		return render(request,"main_firebase/Login.html",{"message":message, "conteudo":conteudo})
	session_id=user['idToken']
	request.session['uid'] = str(session_id)
	#dados= {"email":email}
	return render(request,"main_data/homepage_admin.html",{"conteudo": conteudo,"email":email})

def logout(request):
	try:
		del request.session['uid']
	except:
		pass
	return render(request,"main_firebase/Login.html")

def signUp(request):
	#return HttpResponseRedirect("main_firebase/Registration.html")
	return render(request,"main_firebase/Registration.html")

def postsignUp(request):
	email = request.POST.get('email')
	passs = request.POST.get('pass')
	name = request.POST.get('name')
	try:
		# Criar usuario atravez do email e do password
		user=authe.create_user_with_email_and_password(email,passs)
		uid = user['localId']
		idtoken = request.session['uid']
		print(uid)
	except:
		return render(request, "main_firebase/Registration.html")
	return render(request,"main_firebase/main.html")

def reset(request):
	return render(request, "main_firebase/Reset.html")

def postReset(request):
	email = request.POST.get('email')
	try:
		authe.send_password_reset_email(email)
		message = "Seu email foi revisado com sucesso"
		return render(request, "main_firebase/Reset.html", {"msg":message})
	except:
		message = "Verifique seu Email:, nele haverá um link de confirmação"
		return render(request, "main_firebase/Reset.html", {"msg":message})

def Create(request):
	return render(request, "main_data/create.html")

def PostCreate(request):
	titulo = request.POST.get('txtTitulo')
	subtitulo = request.POST.get('txtSubTitulo')
	autor = request.POST.get('txtAutor')
	texto = request.POST.get('txtTexto')

	data = {
			"titulo": titulo,
			"subtitulo":subtitulo,
			"autor": autor,
			"texto": texto,
	}
	return render(request, "main_data/homepage_admin.html")

def Home_page_admin (request):
	conteudo =SearchConteudos.objects.all()
	return render(request,"main_firebase/Home.html",{"conteudo":conteudo})

#----------------------------------------------------------------------------

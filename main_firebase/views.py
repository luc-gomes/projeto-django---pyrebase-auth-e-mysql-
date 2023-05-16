from django.shortcuts import render
from pyrebase import pyrebase

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

# Initialising database,auth and firebase for further use


firebase=pyrebase.initialize_app(config)
 
authe = firebase.auth()
database=firebase.database()

def signIn(request):
	return render(request,"main_firebase/Login.html")

def home(request):
	#projeto = database.child('Historias').stream()
	#projeto = database.child('Historias').child('Historia').get().val()
	#projeto = database.child('Historias').child('Historia').get().val().keys()
	#projeto = database.child('conteudo').where('visible' == True).stream()
	#projeto = database.child('Historias').child('pqXQUtihItQLqA1dukYk').get().val()
	titulo    = database.child('conteudo').child('conteudo_dicertado').get().val()
    #subtitulo = database.child('Historias').child('subtitulo').get().val()
	sinopse   = database.child('conteudo').child('nome').get().val()
	autor     = database.child('conteudo').child('subtitulo').get().val()

	return render(request,"main_firebase/Home.html",{"autor": autor, "titulo":titulo,  "sinopse":sinopse, "projeto":projeto })




def Main(request):
	return render(request,"main_firebase/main.html")

def postsignIn(request):
	email=request.POST.get('email')
	pasw=request.POST.get('pass')
	try:
		# tentar entrar no auth com email e password
		user=authe.sign_in_with_email_and_password(email,pasw)
	except:
		message="Credenciais invalidas, verifique os dados de entrada"
		return render(request,"Login.html",{"message":message})
	session_id=user['idToken']
	request.session['uid'] = str(session_id)
	return render(request,"main_firebase/Home.html",{"email":email})

def logout(request):
	try:
		del request.session['uid']
	except:
		pass
	return render(request,"main_firebase/Login.html")

def signUp(request):
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
	return render(request,"main_firebase/Login.html")

def reset(request):
	return render(request, "main_firebase/Reset.html")

def postReset(request):
	email = request.POST.get('email')
	try:
		authe.send_password_reset_email(email)
		message = "SEU EMAIL FOI REVISADO COM SUCESSO!"
		return render(request, "main_firebase/Reset.html", {"msg":message})
	except:
		message = "Verifique seu Email:, nele haverá um link de confirmação"
		return render(request, "main_firebase/Reset.html", {"msg":message})
#---------------------------------------------------------------------------------------------------------------------------------------------------
#
#
#---------------------------------------------------------------------------------------------------------------------------------------------------

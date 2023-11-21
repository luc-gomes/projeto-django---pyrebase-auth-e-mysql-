from django.http import HttpResponseRedirect
from django.shortcuts import render
from main_firebase.models import SearchAutores
import pyrebase
from django.db import connection
config={
  "apiKey": "",
  "authDomain": "",
  "databaseURL": "https://",
  "projectId": "",
  "storageBucket": "",
  "messagingSenderId": "",
  "appId": "",
  "measurementId": ""
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
	cursor.execute("SELECT c.titulo, c.subtitulo, c.visibilidade, a.nome, a.sobrenome FROM conteudos c INNER JOIN autores a ON c.codigo_autor = a.codigo_autor where c.visibilidade = 1 order by a.nome;")
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

def Home_page_admin (request):
	
	cursor = connection.cursor()
	cursor.execute("SELECT c.titulo, c.subtitulo, c.visibilidade, a.nome, a.sobrenome FROM conteudos c INNER JOIN autores a ON c.codigo_autor = a.codigo_autor;")
	conteudo = cursor.fetchall()	
	return render(request,"main_firebase/Home.html",{"conteudo":conteudo})

def Tela_sobre (request):
	
	f= open("/home/lucas/Documentos/django/mysite_firebase com serch/mysite_firebase 22may231945/mysite_firebase/mysite/requirements.txt", "r")
	print(f.read())
	lista = {}
	for i in f:
		lista.append(f[i])
	f.close()
	print(lista)
	return render(request,"main_firebase/tela sobre.html",{"lista": lista})

def searchcontent(request):
	
	cursor = connection.cursor()
	cursor.execute(f"SELECT c.titulo, c.subtitulo, c.visibilidade, a.nome, a.sobrenome FROM conteudos c INNER JOIN autores a ON c.codigo_autor = a.codigo_autor where c.visibilidade = 1 and  lower(titulo) like '%{request.POST.get('pesquisa')}%';")
	conteudo = cursor.fetchall()	
	return render(request, "main_firebase/search.html",{"conteudo":conteudo})

def Create(request):
	Autor = SearchAutores.objects.all()	
	return render(request, "main_data/create.html",{"Autor":Autor})

def PostCreate(request):
	message = None
	cursor = connection.cursor()
	Autor = SearchAutores.objects.all()	
	try:

		cursor.execute(f"insert into conteudos(codigo_pb,titulo, subtitulo, texto, visibilidade, codigo_autor) values('{request.POST.get('txtTitulo').lower()}','{request.POST.get('txtSubTitulo').lower()}','{request.POST.get('txtTexto').lower()}', {request.POST.get('checkVisibilidade')}, {request.POST.get('lang_txt')});")
		conteudo = cursor.fetchall()	
	
	except:
		message = 'error'
		return render(request, "main_data/create.html",{"Autor":Autor,"message": message})

	cursor.execute("SELECT c.titulo, c.subtitulo, c.visibilidade, a.nome, a.sobrenome FROM conteudos c INNER JOIN autores a ON c.codigo_autor = a.codigo_autor;")
	conteudo = cursor.fetchall()	
	return render(request,"main_firebase/Home.html",{"conteudo":conteudo})


def Add_autor(request):
	Autor = SearchAutores.objects.all()	
	return render(request, "main_data/add_autor.html",{"Autor":Autor})

def Post_autor(request):
	Autor = SearchAutores.objects.all()	
	cursor = connection.cursor()
	message = None

	try:

		cursor.execute(f"insert into autores (nome, sobrenome, email) values ('{request.POST.get('txtNome_autor').lower()}','{request.POST.get('txtSobrenome_autor').lower()}', '{request.POST.get('txtEmail_Autor').lower()}');")
		conteudo = cursor.fetchall()

	except:
		message = 'erro'
		return render(request, "main_data/add_autor.html",{"Autor":Autor, "message":message})
		
	return render(request, "main_data/create.html",{"Autor": Autor})

# não funciona
def PostDelete(request):
	try:
		data = request.POST.get('data')
		cursor = connection.cursor()
		cursor.execute(f"DELETE FROM conteudo WHERE codigo_conteudo = {data};")
		conteudo = cursor.fetchall()	
	
	except:
		message = 'erro'
		cursor = connection.cursor()
		cursor.execute("SELECT c.titulo, c.subtitulo, c.visibilidade, a.nome, a.sobrenome FROM conteudos c INNER JOIN autores a ON c.codigo_autor = a.codigo_autor;")
		conteudo = cursor.fetchall()	
	
		return render(request,"main_firebase/Home.html",{"conteudo":conteudo,"message":message})


	cursor = connection.cursor()
	cursor.execute("SELECT c.titulo, c.subtitulo, c.visibilidade, a.nome, a.sobrenome FROM conteudos c INNER JOIN autores a ON c.codigo_autor = a.codigo_autor;")
	conteudo = cursor.fetchall()	
	return render(request,"main_firebase/Home.html",{"conteudo":conteudo})

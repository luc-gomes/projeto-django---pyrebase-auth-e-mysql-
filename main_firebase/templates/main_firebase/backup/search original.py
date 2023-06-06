from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import pyrebase

config={
	
	"databaseURL": "*********************",
	"projectId": "*******************",

}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

# move to this search.html page to search for content
def search(request):
	return render(request, "search.html")

# after typing what to search this function will be called
def searchusers(request):
	value = request.POST.get('search')
	
	# if no value is given then render to search.h6tml
	if value =="":
		return render(request, "search.html")
	title = request.POST['category']
	if title =="":
		return render(request, "search.html")
	if value is None or title is None:
		print(value ,"Value",title)
		return render(request, "search.html")
	else:
		if title == "Users":
			data = database.child('users').shallow().get().val()
			uidlist = []
			requid = 'null'
			
			# append all the id in uidlist
			for i in data:
				uidlist.append(i)
				
			# if we have find all the uid then
			# we will look for the one we need
			for i in uidlist:
				val = database.child('users').child(i).child('name').get().val()
				val=val.lower()
				value=value.lower()
				print(val,value)
				
				# if uid we want is value then
				# we will store that in requid
				if (val == value):
					requid = i
			if requid=='null':
				return render(request, "search.html")
			print(requid)
			
			# then we will retrieve all the data related to that uid
			name = database.child('users').child(requid).child('name').get().val()
			course = database.child('users').child(requid).child('course').get().val()
			branch = database.child('users').child(requid).child('branch').get().val()
			img = database.child('users').child(requid).child('imgUrl').get().val()
			Name = []
			Name.append(name)
			Course = []
			Course.append(course)
			Branch = []
			Branch.append(branch)
			Image = []
			Image.append(img)
			comb_lis = zip(Name, Course, Branch, Image)
			
			# send all data in zip form to searchusers.html
			return render(request, "SearchUsers.html", {"comb_lis": comb_lis})

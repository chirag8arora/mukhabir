from django.http import HttpResponse, HttpResponseRedirect,Http404
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout
# from django.contrib import messages,auth
# from django.contrib.auth import authenticate
from django.shortcuts import render_to_response, get_object_or_404, redirect,render
from django.core.context_processors import csrf
from django.template import RequestContext
from .models import *
from empts.forms import *
from django.db.models import Q
import requests
import json
# from empts.backends import *

# @login_required
def login(request):
	c={}
	c.update(csrf(request))
	return render_to_response('registration/login.html',c)

	 # user=authenticate(username=username,password=password)
	 # if user is not None:
	 # 	auth.login(request,user)
	 # 	return render_to_response('loggedin.html',{'user':request.user})

def loggedin(request):
	query=Manager.objects.all()
	query1=Employee.objects.all()
	username=request.POST.get('username')
	password=request.POST.get('password')
	print (username)
	data={
		'username':request.POST.get('username'),
		'password':request.POST.get('password'),
	}
	url = "http://localhost:8000/api/u/"
	x = requests.post(url,data=json.dumps(data))
	
	data = x.json()
	print (x.status_code)
	print (x.headers)
	print (data[0]['username'])

	url = "http://localhost:8000/api/u/a"+str(data[0]['id'])+'/'
	x=requests.get(url)
	data1 = x.json()
	print(data1)
	url = "http://localhost:8000/api/u/l"+str(data[0]['id'])+'/'
	x=requests.get(url)
	data2 = x.json();
	print(data);
	if x:
		if data:
			context={
			'data': data[0],
			'user': data1[0],
			'locations' : data2[0]
			}
			request.session['id']=username
			return render(request,'loggedin.html',context)
		else:
			return render_to_response('invalid_login.html',{})
# 	username=request.POST.get('username','')
# 	password=request.POST.get('password','')
# 	user=authenticate(username=username,password=password)

# 	# if user is not None:
# 	# 	auth.login(request,user)
# 	# 	return HttpResponseRedirect('/loggedin')
# 	# else:
# 	# 	return HttpResponseRedirect('/invalid')
# 	return render_to_response(
#     'loggedin.html',
#     { 'user': request.user }
#     )

# def loggedin(request):
# 	# query=Manager.objects.filter(manager_id=request.user.username)
# 	# context={
# 	# "object_list":query,
# 	# }
# 	return render_to_response("loggedin.html",{'user':request.user})

# def invalid_login(request):
# 	 return render_to_response('invalid_login.html')
	

def logout(request):
	# auth.logout(request)
	del request.session['id']
	return HttpResponseRedirect('/')



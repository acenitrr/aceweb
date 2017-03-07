from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from login.models import *
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.contrib.auth.views import login,logout

def get_notice(request):
	response={}
	json_list=[]
	for o in notice_data.objects.all():
		if(o.active==True):
			tmp_json={}
			tmp_json['title']=o.title
			tmp_json['content']=o.content
			tmp_json['issuer']=o.issuer
			tmp_json['file']=str(o.file)
			tmp_json['date']=o.date_issued
			tmp_json['created']=o.created
			json_list.append(tmp_json)

	response['list']=json_list
	print response
	return JsonResponse(response)

def home(request):
	if request.user.is_authenticated():
		return render(request,'index.html' ,{'link1':'<a href="/profile/">PROFILE</a>','link2':'<a href="/logout/">LOGOUT</a>'})
	else:
		return render(request,'index.html',{'link2':'<a href="/login/">LOGIN</a>'})

# def academics(request):
# 	return render(request,'academics.html')

def activities(request):
	if request.user.is_authenticated():
		return render(request,'activities.html' ,{'link1':'<a href="/profile/">PROFILE</a>','link2':'<a href="/logout/">LOGOUT</a>'})
	else:
		return render(request,'activities.html',{'link2':'<a href="/login/">LOGIN</a>'})

def administration(request):
	if request.user.is_authenticated():
		return render(request,'faculty.html' ,{'link1':'<a href="/profile/">PROFILE</a>','link2':'<a href="/logout/">LOGOUT</a>'})
	else:
		return render(request,'faculty.html',{'link2':'<a href="/login/">LOGIN</a>'})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

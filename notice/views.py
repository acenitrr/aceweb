from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from login.models import *
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse

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
	return render(request,'index.html')

def academics(request):
	return render(request,'academics.html')

def administration(request):
	return render(request,'faculty.html')

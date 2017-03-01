from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from login.models import *
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse



def get_announcement(request):
	response={}
	json_list=[]
	for o in announcement_data.objects.all():
		if(o.active==True):
			tmp_json={}
			tmp_json['title']=o.title
			tmp_json['content']=o.content
			tmp_json['issuer']=o.issuer
			tmp_json['file']=o.file
			tmp_json['date']=o.date
			tmp_json['created']=o.created
			json_list.append(tmp_json)

	return JsonResponse(response)
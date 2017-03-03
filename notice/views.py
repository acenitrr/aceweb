from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from login.models import *
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse

# def get_notice(request):
# 	response={}
# 	json_list=[]
# 	for o in notice_data.objects.all():
# 		if(o.active==True):
# 			tmp_json={}
# 			tmp_json['title']=o.title
# 			tmp_json['content']=o.content
# 			tmp_json['issuer']=o.issuer
# 			tmp_json['file']=o.file
# 			tmp_json['date']=o.date
# 			tmp_json['created']=o.created
# 			json_list.append(tmp_json)

# 	return JsonResponse(response)

def get_notice(request):
	notice_string=''
	for o in notice_data.objects.all():
		if(o.active==True):
			notice_temp_string="""<p>&#9733%s</p>
		"""
			notice_string+=notice_temp_string % (o.content)	
	return render(request,'index.html' ,{'notice_string':notice_string})

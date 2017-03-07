from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from login.models import *
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse



def project(request):
	# try:
	project_string=''
	flag=0
	temp_obj={}
	for o in project_data.objects.all().order_by('title'):
		if(o.active==True):
			if flag==0:
				project_temp_string="""<B><u>a.)%s:</u></b>%s<br>"""
				flag=1	
				temp_obj=o
				project_string+=project_temp_string % (o.title,o.content)
			else:
				if  o.title==temp_obj.title:
					project_temp_string="""<B></b>%s<br>"""
					project_string+=project_temp_string % (o.content)
				else:
					project_temp_string="""<B><u>a.)%s:</u></b>%s<br>"""
					project_string+=project_temp_string % (o.title,o.content)
					temp_obj=o
	if request.user.is_authenticated():
		return render(request,'academics.html' ,{'project_string':project_string,'link1':'<a href="/profile/">PROFILE</a>','link2':'<a href="/logout/">LOGOUT</a>'})
	else:
		return render(request,'academics.html',{'link2':'<a href="/login/">LOGIN</a>'})
	# except:
	# 	return render(request,'activities.html' ,{'announcement_string':'No upcoming activities'})
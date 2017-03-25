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
				project_temp_string="""<B style="font-size:1.6em;position:relative;left:.1em;">	&#9755%s:</b><hr><div style="font-size:1.5em;">%s</div>"""
				flag=1	
				temp_obj=o
				project_string+=project_temp_string % (o.title,o.content)
			else:
				if  o.title==temp_obj.title:
					project_temp_string="""<B style="font-size:1.9em;float:left;"></b><div style="font-size:1.5em;">%s</div><hr>"""
					project_string+=project_temp_string % (o.content)
				else:
					project_temp_string="""<B style="font-size:1.9em;">	&#9755%s:<hr></b><div style="font-size:1.5em;">%s</div>"""
					project_string+=project_temp_string % (o.title,o.content)
					temp_obj=o
			print "project added"
	print project_string
	if request.user.is_authenticated():
		return render(request,'academics.html' ,{'project_string':project_string,'link2':'<a href="/logout/">LOGOUT</a>'})
	else:
		return render(request,'academics.html',{'project_string':project_string,'link2':'<a href="/login/">LOGIN</a>'})
	# except:
	# 	return render(request,'activities.html' ,{'announcement_string':'No upcoming activities'})
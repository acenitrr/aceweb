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
			tmp_json['url']='/notice_read?id='+str(o.id)
			json_list.append(tmp_json)

	response['list']=json_list
	print response
	return JsonResponse(response)

def notice_read(request):
	tmp_json={}
	tmp_json['title']=''
	tmp_json['content']=''
	tmp_json['issuer']=''
	tmp_json['file']=''
	tmp_json['date']=''
	tmp_json['created']=''
	try:
		notice_row=notice_data.objects.get(id=int(request.GET.get('id')))
		if(notice_row.active==True):
			tmp_json['title']=notice_row.title
			tmp_json['content']=notice_row.content
			tmp_json['issuer']=notice_row.issuer
			tmp_json['file']=''
			if(notice_row.file!=None):
				tmp_json['file']='file:<a href="'+str(request.scheme+'://'+request.get_host())+'/'+str(notice_row.file)+'" download>Download File</a>'

			tmp_json['date']=notice_row.date_issued
			tmp_json['created']=str(notice_row.created)[:19]
	except Exception,e:
		print e
	return render(request,'notice.html',tmp_json)

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

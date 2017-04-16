from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from login.models import *
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.contrib.auth.views import login,logout
from login.models import *
from django.core.mail import EmailMessage,get_connection
from custom_key.models import *
from django.core.mail.backends.smtp import EmailBackend

#Group_id distributions
# 1 - student
# 2 - faculty
# 3 - alumni
# 4 - admin
# 5 - developer

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

def get_profile(request):
	response={}
	if request.user.is_authenticated():
		login_id=str(request.user)
		login_data_row=login_data.objects.get(login_id=login_id)
		link1='<div class="dropdown"><button class="dropbtn"><div style="font-size:0.95em;color:#9d9d9d;font-family:arial;">PROFILE</div></button><div class="dropdown-content">'
		if login_data_row.group_id==1:
			link1+='<a href="/student_view/'+str(request.user)+'" >MY PROFILE</a>'
		else:
			if login_data_row.group_id==2:
				link1+='<a href="/faculty_view/'+str(request.user)+'" >MY PROFILE</a>'
			else:
				if login_data_row.group_id==3:
					link1+='<a href="/alumni_view/'+str(request.user)+'" >MY PROFILE</a>'
				else:
					print 'you are admin or developer'
					link1+='<a href="/" >MY PROFILE</a>'			
		link1+='<a href="/students_profile">STUDENTS</a><a href="/alumni_profile">ALUMNI</a></div></div>'
		print link1
	else:
		link1=''
	print link1
	response['list']=link1
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
				tmp_json['file']='file:<a href="'+str(request.scheme+'://'+request.get_host())+'/media/'+str(notice_row.file)+'" download>Download File</a>'

			tmp_json['date']=notice_row.date_issued
			tmp_json['created']=str(notice_row.created)[:19]
	except Exception,e:
		print e
	if request.user.is_authenticated():
		login_data_row=login_data.objects.get(login_id=str(request.user))
		tmp_json['link2']='<a href="/logout/">LOGOUT</a>'
		return render(request,'notice.html' ,tmp_json)
	else:
		tmp_json['link2']='<a href="/login/">LOGIN</a>'
		return render(request,'notice.html',tmp_json)
def home(request):
	if request.user.is_authenticated():
		return render(request,'index.html' ,{'link2':'<a href="/logout/">LOGOUT</a>'})
	else:
		return render(request,'index.html',{'link2':'<a href="/login/">LOGIN</a>'})

# def academics(request):
# 	return render(request,'academics.html')

def activities(request):
	if request.user.is_authenticated():
		return render(request,'activities.html' ,{'link2':'<a href="/logout/">LOGOUT</a>'})
	else:
		return render(request,'activities.html',{'link2':'<a href="/login/">LOGIN</a>'})

def administration(request):
	if request.user.is_authenticated():
		return render(request,'faculty.html' ,{'link2':'<a href="/logout/">LOGOUT</a>'})
	else:
		return render(request,'faculty.html',{'link2':'<a href="/login/">LOGIN</a>'})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

@csrf_exempt
def contact_view(request):
	try:
		login_id="none"
		if request.user.is_authenticated():
			login_id=str(request.user)
		else:
			pass
		if request.method=="POST":
			name=str(request.POST.get('name'))
			email=str(request.POST.get('email'))
			mobile=str(request.POST.get('mobile'))
			sub=str(request.POST.get('sub'))
			msg=str(request.POST.get('msg'))
			msg+="""


By :
name : %s
email: %s
mobile : %s
login_id : %s"""

			msg = msg %(name,email,mobile,login_id)
			try:
				host=custom_key_data.objects.get(key='host').value
				print host
				port=custom_key_data.objects.get(key='port').value
				username=custom_key_data.objects.get(key='username').value
				password=custom_key_data.objects.get(key='password').value
				con_email=custom_key_data.objects.get(key='con_email').value
				fac_email=custom_key_data.objects.get(key='fac_email').value
				print fac_email
				email=[]
				email+=[username]+[con_email]+[fac_email]
				print email
				backend = EmailBackend(host=str(host), port=int(port), username=str(username), 
				                       password=str(password), use_tls=True, fail_silently=True)
				email_msg= EmailMessage(sub,msg,'no-reply@gmail.com',bcc=email,connection=backend)
				email_msg.send()
				return render (request,'contact.html',{'msg':'Your feedback/query is submitted'})
			except Exception,e:
				print e
				return render(request,'contact.html',{'msg':'some error occur please try again'})
		else:
			if request.user.is_authenticated():
				return render(request,'contact.html' ,{'link2':'<a href="/logout/">LOGOUT</a>'})
			else:
				return render(request,'contact.html',{'link2':'<a href="/login/">LOGIN</a>'})
	except Exception,e:
		print e
		return render(request,'contact.html',{'msg':'some error occur please try again'})


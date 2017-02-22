from django.shortcuts import render
from student.models import *
from faculty.models import *
from alumni.models import *
from login.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
import jwt
from internal_key.models import *
from custom_key.models import *
from django.core.mail import EmailMessage,get_connection
from django.core.mail.backends.smtp import EmailBackend
from django.contrib.auth.models import User

@csrf_exempt
def forgot_password_view(request):
	if request.user.is_authenticated():
		return render (request,'welcome.html')
	else:
		if request.method=='POST':
			login_id=str(request.POST.get('login_id'))
			email=str(request.POST.get('email'))
			try:
				login_row=login_data.objects.get(login_id=login_id)
				group_id=login_row.group_id
				if group_id==1:
					try:
						student_data_row=student_data.objects.get(roll_no=login_id)
						student_email=str(student_data_row.email)
						student_name=str(student_data_row.name)
						print student_email
						print student_name
						if student_email==str(email):
							jwt_key=str(internal_key_data.objects.get(key='jwt_key').value)
							print jwt_key
							login_JSON={'login_id':login_id}
							login_encode=jwt.encode(login_JSON,jwt_key,algorithm='HS256')
							print login_encode
							link_url=str(request.scheme+'://'+request.get_host()+'/verify_forgot_password/'+login_encode)
							url='<a href='+link_url+'>verify email</a>'
							host_email=str(custom_key_data.objects.get(key='host').value)
							port_email=str(custom_key_data.objects.get(key='port').value)
							username_email=str(custom_key_data.objects.get(key='username').value)
							password_email=str(custom_key_data.objects.get(key='password').value)
							body=str(email_send_data.objects.get(key='forgot_email').email_data)
							backend = EmailBackend(host=str(host_email), port=int(port_email), username=str(username_email), 
			                       password=str(password_email), use_tls=True, fail_silently=True)
							EmailMsg=EmailMessage("ACE",body % (student_name,url) ,'no-reply@gmail.com',[student_email] ,connection=backend)
							EmailMsg.content_subtype = "html"
							EmailMsg.send()
							return render(request,'forgot_email.html',{'msg':'email is send to your register email_id'})
						else:
							return render (request,'forgot_email.html',{'msg':'Please enter registered email_id'})
					except:
						return render (request,'forgot_email.html',{'msg':'Invalid login_id'})
				else:
					if group_id==2:
						try:
							faculty_data_row=faculty_data.objects.get(faculty_id=login_id)
							faculty_email=faculty_data_row.email
							faculty_name=faculty_data_row.name
							if faculty_email==email:
								login_JSON={'login_id':login_id}
								jwt_key=str(internal_key_data.objects.get(key='jwt_key').value)
								login_encode=jwt.encode(login_JSON,jwt_key,algorithm='HS256')
								print login_encode
								link_url=str(request.scheme+'://'+request.get_host()+'/verify_forgot_password/'+login_encode)
								url='<a href='+link_url+'>verify email</a>'
								host_email=str(custom_key_data.objects.get(key='host').value)
								port_email=str(custom_key_data.objects.get(key='port').value)
								username_email=str(custom_key_data.objects.get(key='username').value)
								password_email=str(custom_key_data.objects.get(key='password').value)
								body=str(email_send_data.objects.get(key='forgot_email').email_data)
								backend = EmailBackend(host=str(host_email), port=int(port_email), username=str(username_email), 
				                       password=str(password_email), use_tls=True, fail_silently=True)
								EmailMsg=EmailMessage("ACE",body % (faculty_name,url) ,'no-reply@gmail.com',[faculty_email] ,connection=backend)
								EmailMsg.content_subtype = "html"
								EmailMsg.send()
								return render(request,'forgot_email.html',{'msg':'email is send to your register email_id'})
							else:
								return render (request,'forgot_email.html',{'msg':'Please enter registered email_id'})
						except:
							return render (request,'forgot_email.html',{'msg':'Invalid login_id'})
					else:
						if group_id==3:
							try:
								alumni_data_row=alumni_data.objects.get(roll_no=login_id)
								alumni_email=alumni_data_row.email
								alumni_name=alumni_data_row.name
								if alumni_email==email:
									login_JSON={'login_id':login_id}
									jwt_key=str(internal_key_data.objects.get(key='jwt_key').value)
									login_encode=jwt.encode(login_JSON,jwt_key,algorithm='HS256')
									print login_encode
									link_url=str(request.scheme+'://'+request.get_host()+'/verify_forgot_password/'+login_encode)
									url='<a href='+link_url+'>verify email</a>'
									host_email=str(custom_key_data.objects.get(key='host').value)
									port_email=str(custom_key_data.objects.get(key='port').value)
									username_email=str(custom_key_data.objects.get(key='username').value)
									password_email=str(custom_key_data.objects.get(key='password').value)
									body=str(email_send_data.objects.get(key='forgot_email').email_data)
									backend = EmailBackend(host=str(host_email), port=int(port_email), username=str(username_email), 
					                       password=str(password_email), use_tls=True, fail_silently=True)
									EmailMsg=EmailMessage("ACE",body % (alumni_name,url) ,'no-reply@gmail.com',[alumni_email] ,connection=backend)
									EmailMsg.content_subtype = "html"
									EmailMsg.send()
									return render(request,'forgot_email.html',{'msg':'email is send to your register email_id'})
								else:
									return render (request,'forgot_email.html',{'msg':'Please enter registered email_id'})
							except:
								return render (request,'forgot_email.html',{'msg':'Invalid login_id'})
						else:
							return render(request,'forgot_email.html',{'msg':'invalid login_id'})
			except:
				return render(request,'forgot_email.html',{'msg':'invalid login_id'})
		else:
			return render(request,'forgot_email.html')


@csrf_exempt
def verify_forgot_password(request,value):
	if request.user.is_authenticated():
		return render (request,'welcome.html')
	else:
		try:
			jwt_key=str(internal_key_data.objects.get(key='jwt_key').value)
			login_JSON_decode=jwt.decode(value,jwt_key,algorithms=['HS256'])
			login_id=login_JSON_decode['login_id']
			print login_id
			return change_password(request,login_id) 
		except:
			return HttpResponse('Failed')

@csrf_exempt
def change_password(request,login_id):
	if request.user.is_authenticated():
		return render (request,'welcome.html')
	else:
		if request.method=='POST':
			try:
				password=str(request.POST.get('password'))
				print password
				user_row=User.objects.get(username=str(login_id))
				user_row.set_password(str(password))
				user_row.save()
				return render(request,'change_password.html',{'msg':'password is changed'})
			except:
				return render(request,'change_password.html',{'msg':'somthing occur Please try again'})
		else:
			return render(request,'change_password.html')













# Create your views here.

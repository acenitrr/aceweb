from django.shortcuts import render
from .models import login_data
import jwt
import random 
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseBadRequest
from django.contrib.auth import authenticate, login,logout
from django.core.mail import EmailMessage,get_connection
from custom_key.models import *
from django.core.mail.backends.smtp import EmailBackend
from internal_key.models import *
from student.models import *
from faculty.models import *
from alumni.models import *
from student.views import signup_student

class UploadFileForm(forms.Form):
    file = forms.FileField()

#Group_id distributions
# 1 - student
# 2 - faculty
# 3 - alumni
# 4 - admin
# 5 - developer
@login_required
@csrf_exempt
def import_login_table(request):
	if request.user.is_authenticated():
		user=str(request.user)
		try:
			login_data_row=login_data.objects.get(login_id=str(user))
			if login_data_row.group_id==5:
			    if request.method == "POST":
			    	print "27"
			        form = UploadFileForm(request.POST,request.FILES)
			        if form.is_valid():
			        	print "30"
			        	request.FILES['file'].save_to_database(model=login_data,mapdict=['login_id','group_id'])
			        	return HttpResponse("OK")
			        else:
			            return HttpResponseBadRequest()
			    else:
			        form = UploadFileForm()
			        return render(request,'upload.html',{'form':form})
		except:
			return HttpResponse("Page not found")
	else:
		return HttpResponse("page not found")


def email_verification(request,value):
	try:
		print value
		jwt_key=str(internal_key_data.objects.get(key='jwt_key').value)
		print jwt_key
		email_decoded_json=jwt.decode(value,jwt_key,algorithms =['HS256'])
		print email_decoded_json
		email=email_decoded_json['email']
		roll_no=email_decoded_json['roll_no']
		# otp=jwt.decode(otp,'secret',algorithms=['HS256'])
		print email
		print roll_no
		# print otp
		try:
			login_data_row=login_data.objects.get(email=email)
			group_id=login_data_row.group_id
			setattr(login_data_row,'email_flag',True)
			login_data_row.save()
			if group_id==1:
				return render(request,'signup_student.html',{'login_id':roll_no})
			else:
				if group_id==2:
					return render(request,'signup_faculty.html',{'login_id':roll_no})
				else:
					if group_id==3:
						return render(request,'signup_alumni.html',{'login_id':roll_no})
					else:
						return HttpResponse("ok")
		except Exception,e:
			print e
			return HttpResponse("email_id already registered try another or contact ace ")
	except:
		return HttpResponse("Failed")

# http://127.0.0.1:8000/verify_email?email=arpitj938@gmail.com&otp=123456
@csrf_exempt
def login_view(request):
	if request.user.is_authenticated():
		return render (request,'index.html',{'link1':'<a href="/profile/">PROFILE</a>','link2':'<a href="/logout/">LOGOUT</a>'})
	else:
		if request.method=='POST':
			login_id=str(request.POST.get('login_id'))
			print login_id
			password=str(request.POST.get('password'))
			# password=jwt.decode(password,'secret',algorithms=['HS256'])
			try:
				login_data_row=login_data.objects.get(login_id=login_id)
				print login_id
				if login_data_row.email_flag==1:
					print 105
					user = authenticate(username=login_id, password=password)
					if user is not None:
						login(request, user)
						print 'login done'
						return render (request,'index.html',{'link1':'<a href="/profile/">PROFILE</a>','link2':'<a href="/logout/">LOGOUT</a>'})
						# return HttpResponseRedirect("/welcome/")
					else:
						return render(request,'login.html',{'login_status':'wrong login_id or password'})
				else:
					return render(request,'login.html',{'login_status':'complete your email verification'})
			except:
				return render(request,'login.html',{'login_status':'wrong login_id or password'})
		else:
			return render(request,'login.html')

@csrf_exempt
def signup_view(request):
	if request.user.is_authenticated():
		return render (request,'index.html',{'link1':'<a href="/profile/">PROFILE</a>','link2':'<a href="/logout/">LOGOUT</a>'})
	else:
		if request.method=='POST':
			try:
				print "try"
				# roll_no='151258'
				roll_no=str(request.POST.get('roll_no'))
				print roll_no
				# name='arpit'
				name=str(request.POST.get('name'))
				print name
				mobile=str(request.POST.get('mobile'))
				email=str(request.POST.get('email'))
				# email='arpitj938@gmail.com'
				print email
				try:
					print "try 1"
					login_data_row=login_data.objects.get(login_id=roll_no)
					group_id=login_data_row.group_id
					print group_id
					if login_data_row.email_flag==True:
						print 'your account is registered already'
						# return HttpResponse("your account is registered already")
						return render(request,"signup.html",{'msg':'your account is registered already','link2':'<a href="/login/">LOGIN</a>'})	
					else:
						print roll_no
						if group_id==1:
							try:
								student_data_row=student_data.objects.get(roll_no=roll_no)
								setattr(student_data_row,'name',str(name))
								setattr(student_data_row,'mobile',str(mobile))
								setattr(student_data_row,'email',str(email))
								student_data_row.save()
							except:
								student_data.objects.create(roll_no=roll_no,name=name,email=email,mobile=mobile)
								print '148'
						else:
							if group_id==2:
								try:
									faculty_data_row=faculty_data.objects.get(faculty_id=roll_no)
									setattr(faculty_data_row,'name',str(name))
									setattr(faculty_data_row,'mobile',str(mobile))
									setattr(faculty_data_row,'email',str(email))
									faculty_data_row.save()
								except:
									faculty_data.objects.create(faculty_id=roll_no,name=name,email=email,mobile=mobile)
							else:
								if group_id==3:
									try:
										alumni_data_row=alumni_data.objects.get(roll_no=roll_no)
										setattr(alumni_data_row,'name',str(name))
										setattr(alumni_data_row,'mobile',str(mobile))
										setattr(alumni_data_row,'email',str(email))
										alumni_data_row.save()
									except:
										alumni_data.objects.create(roll_no=roll_no,name=name,email=email,mobile=mobile)
						setattr(login_data_row,'email',str(email))
						login_data_row.save()
						print '160'
						host_email=str(custom_key_data.objects.get(key='host').value)
						port_email=custom_key_data.objects.get(key='port').value
						username_email=str(custom_key_data.objects.get(key='username').value)
						password_email=str(custom_key_data.objects.get(key='password').value)
						print host_email
						email_json={'email':str(email),
						'roll_no':str(roll_no)}
						jwt_key=str(internal_key_data.objects.get(key='jwt_key').value)
						email_encoded_url=jwt.encode(email_json,jwt_key,algorithm='HS256')
						print email_encoded_url
						link=str(request.scheme+"://"+request.get_host()+"/verify_email/"+email_encoded_url)
						url='<a href='+link+'>verify email</a>'
						# image='<img src='+'"https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTEgRR_jTgKgGkHyVYFbXHg51pzhpWmx1bsgREGMcV621HdH39q"'+'>'
						print url
						# email_body=str(custom_keys_data.objects.get(key='email_test').value)
						email_body=str(custom_key_data.objects.get(key='email_verify').value)
						print email_body % (name,url)
						backend = EmailBackend(host=str(host_email), port=int(port_email), username=str(username_email), 
			                       password=str(password_email), use_tls=True, fail_silently=True)
						EmailMsg=EmailMessage("ACE",email_body % (name,url) ,'no-reply@gmail.com',[email] ,connection=backend)
						EmailMsg.content_subtype = "html"
						EmailMsg.send()
						return render(request,"signup.html",{'msg':'email is send to your email account kindly verify it','link2':'<a href="/login/">LOGIN</a>'})
				except:
					print 'enroll_no is not valid'
					return render(request,"signup.html",{'msg':'enroll_no is not valid','link2':'<a href="/login/">LOGIN</a>'})
			except:
				print 'enroll_no not get'
				return render(request,"signup.html",{'msg':'enroll_no not get','link2':'<a href="/login/">LOGIN</a>'})
		else:
			return render(request,"signup.html",{'link2':'<a href="/login/">LOGIN</a>'})
@login_required
def ping(request,id):
	return render (request,'ping.html',{'link1':'<a href="/profile/">PROFILE</a>','link2':'<a href="/logout/">LOGOUT</a>','roll_no':id})
	
@login_required
@csrf_exempt
def ping_send(request):
	try:
		if request.method=='POST':
			msg=str(request.POST.get('msg'))
			id=str(request.POST.get('roll_no'))
			login_id=str(request.user)
			login_data_row=login_data.objects.get(login_id=login_id)
			login_data_row_2=login_data.objects.get(login_id=id)
			sender_group_id=login_data_row.group_id
			reciver_group_id=login_data_row_2.group_id
			if sender_group_id==1:
				sender_data_row=student_data.objects.get(roll_no=login_id)
				sender_name=sender_data_row.name
				sender_mobile=sender_data_row.mobile
			else:
				if sender_group_id==2:
					sender_data_row=faculty_data.objects.get(faculty_id=login_id)
					sender_name=sender_data_row.name
					sender_mobile=sender_data_row.mobile
				else:
					if sender_group_id==3:
						sender_data_row=alumni_data.objects.get(roll_no=login_id)
						sender_name=sender_data_row.name
						sender_mobile=sender_data_row.mobile
			if reciver_group_id==1:
						reciver_data_row=student_data.objects.get(roll_no=id)
						reciver_name=reciver_data_row.name
			else:
				if reciver_group_id==3:
					reciver_data_row=alumni_data.objects.get(roll_no=id)
					reciver_name=reciver_data_row.name
			reciver_email=login_data_row_2.email
			sender_email=login_data_row.email
			host_email=str(custom_key_data.objects.get(key='host').value)
			port_email=custom_key_data.objects.get(key='port').value
			username_email=str(custom_key_data.objects.get(key='username').value)
			password_email=str(custom_key_data.objects.get(key='password').value)
			email_body=str(custom_key_data.objects.get(key='email_connect').value)
			print email_body % (reciver_name,sender_name,msg,sender_mobile,sender_email)
			backend = EmailBackend(host=str(host_email), port=int(port_email), username=str(username_email), 
	                   password=str(password_email), use_tls=True, fail_silently=True)
			EmailMsg=EmailMessage("ACE",email_body % (reciver_name,sender_name,msg,sender_mobile,sender_email) ,'no-reply@gmail.com',[reciver_email] ,connection=backend)
			EmailMsg.content_subtype = "html"
			EmailMsg.send()
			return render (request,'ping.html',{'msg':'email is send, kindly wait for reply','link1':'<a href="/profile/">PROFILE</a>','link2':'<a href="/logout/">LOGOUT</a>'})
	except:
		return render (request,'ping.html',{'msg':'Something occur please try again','link1':'<a href="/profile/">PROFILE</a>','link2':'<a href="/logout/">LOGOUT</a>'})
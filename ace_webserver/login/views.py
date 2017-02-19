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
from keys.models import *
from django.core.mail.backends.smtp import EmailBackend

class UploadFileForm(forms.Form):
    file = forms.FileField()

@login_required
@csrf_exempt
def import_login_table(request):
	if request.user.is_authenticated():
		user=str(request.user)
		try:
			login_data_row=login_data.objects.get(login_id=str(user))
			if login_data_row.group_id=='admin':
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


def email_verification(request):
	try:
		#email=str(request.GET.get('email'))
		#tp=str(request.GET.get('otp'))
		#group_id=str(request.GET.get('group_id'))
		email_decoded_json=jwt.decode(email,'secret',algorithms=['HS256'])
		email=email_decoded_json['email']
		roll_no=email_decoded_json['roll_no']
		# otp=jwt.decode(otp,'secret',algorithms=['HS256'])
		print email
		print otp
		try:
			login_data_row=login_data.objects.get(email=email)
			if login_data_row.otp==otp:
				setattr(login_data_row,'email_flag',True)
				login_data_row.save()
				if group_id=="student":
					return HttpResponse("student signup")
				else:
					if group_id=="faculty":
						return HttpResponse("faculty signup")
					else:
						if group_id=="alumni":
							return HttpResponse("alumni signup")
			else:
				return HttpResponse("email verification not done")
		except:
			return HttpResponse("email_id and otp not get")
	except:
		return HttpResponse("Failed")

# http://127.0.0.1:8000/verify_email?email=arpitj938@gmail.com&otp=123456

def login_view(request):
	if request.user.is_authenticated():
		return render(request,'main.html',{'logout':'logout'})
	else:
		if request.method=='POST':
			login_id=str(request.POST.get('login_id'))
			password=str(request.POST.get('password'))
			# password=jwt.decode(password,'secret',algorithms=['HS256'])
			try:
				login_data_row=login_data.objects.get(login_id=login_id)
				print login_id
				if login_data_row.password==password:
					if login_data_row.email_flag==1:
						user = authenticate(username=login_id, password=password)
						if user is not None:
							login(request, user)
							print 'login done'
							return HttpResponseRedirect("/welcome/")
						else:
							return render(request,'main.html',{'login_status':'wrong login_id or password'})
					else:
						return render(request,'main.html',{'login_status':'complete your email verification'})
				else:
					return render(request,'main.html',{'login_status':'wrong login_id or password'})
			except:
				return render(request,'main.html',{'login_status':'wrong login_id or password'})
		else:
			return render(request,'main.html')

@csrf_exempt
def signup_view(request):
	if request.user.is_authenticated():
		return render(request,'welcome.html')
	else:
		if request.method=='POST':
			try:
				print "try"
				roll_no=str(request.POST.get('roll_no'))
				print roll_no
				name=str(request.POST.get('name'))
				print name
				mobile=str(request.POST.get('mobile'))
				email=str(request.POST.get('email'))
				print email
				otp=str(random.randint(111111,999999))
				try:
					print "try 1"
					login_data_row=login_data.objects.get(login_id=roll_no)
					group_id=str(login_data_row.group_id)
					if login_data_row.email is None:
						print roll_no
						setattr(login_data_row,'otp',int(otp))
						setattr(login_data_row,'email',str(email))
						login_data_row.save()
						key_data_row=keys_data.objects.get(flag=True)
						email_json={'id':email,
						'roll_no':roll_no}
						email_encoded_url=jwt.encode(email,'abc123s',algorithms=['HS256'])
						link=""+"/verify_email/"+email_encoded_url
						body="""welcome %s to Association of Computer engg.

kindly click on the link below to complete email verifications
%s

Thanks and Regards,
ACE , NIT Raipur"""
						print body % (name,link)
						backend = EmailBackend(host=str(key_data_row.host), port=int(key_data_row.port), username=str(key_data_row.username), 
			                       password=str(key_data_row.password), use_tls=True, fail_silently=True)
						EmailMsg=EmailMessage("ACE",body % (name,link),'no-reply@gmail.com',[email] ,connection=backend)
						EmailMsg.send()
						return HttpResponse("done")
					else:
						if login_data_row.email_flag==True:
							return HttpResponse(request,"signup.html",{'msg':'your account is registered already'})
						else:
							return HttpResponse(request,"signup.html",{'msg':'your account is pending for email verification'})
				except:
					return render(request,"signup.html",{'msg':'enroll_no is not valid'})
			except:
				return render(request,"signup.html",{'msg':'enroll_no not get'})
		else:
			return render(request,"signup.html")

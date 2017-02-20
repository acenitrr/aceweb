from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import os

@csrf_exempt
def signup_student(request):
	if request.user.is_authenticated():
		return render (request,'welcome.html')
	else:
		if request.method=="POST":
			try:
				response={}
				login_id=str(request.POST.get('roll_no'))
				sem=str(request.POST.get('sem'))
				github_url=str(request.POST.get('github_url'))
				linkedin_url=str(request.POST.get('linkedin_url'))
				# image=request.FILES.get('photo').name
				# try:
				# 	folder = 'media/student_images/'+roll_no+'/'
				# 	os.mkdir(os.path.join(folder))
				# 	break
				# except:
				# 	response['success']=False
				# print "image=",image
				# fout = open(folder+image, 'w')
				# file_content = request.FILES.get('photo').read()
				# fout.write(file_content)
				# fout.close()
				skill=str(request.POST.get('skill'))
				password=str(request.POST.get('password'))
				try:
					student_data_row=student_data.objects.get(roll_no=login_id)
					setattr(student_data_row,'sem',str(sem))
					setattr(student_data_row,'github_url',str(github_url))
					setattr(student_data_row,'linkedin_url',str(linkedin_url))
					setattr(student_data_row,'skill',str(skill))
					#image pending
					student_data_row.save()
					User.objects.create_user(username=login_id,password=password)
				except:
					return HttpResponse('Invalid login id')
			except:
				return HttpResponse("Data not get")
		else:
			return render(request,'signup_student.html')



def user_profile(request):
	login_id=str(request.user)
	print login_id
	student_data_row=student_data.objects.get(roll_no=login_id)
	skill=str(student_data_row.skill)
	print skill
	return render(request,'show_profile.html',{'skill':skill})



# Create your views here.

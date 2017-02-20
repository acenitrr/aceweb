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


@login_required
def student_profile(request,roll_no):
	try:
		JSON_response={}
		login_id=str(request.user)
		if login_id==roll_no:
			JSON_response['login_id']=login_id
			student_data_row=student_data.objects.get(roll_no=roll_no)
			JSON_response['name']=student_data_row.name
			JSON_response['mobile']=student_data_row.mobile
			JSON_response['email']=student_data_row.email
			JSON_response['sem']=student_data_row.sem
			photo=str(student_data_row.photo)
			photo_url='<img src='+'"/media/'+photo+'"'+'>'
			JSON_response['photo']=photo_url
			print photo_url
			JSON_response['skill']=student_data_row.skill
			JSON_response['linkedin_url']=student_data_row.linkedin_url
			JSON_response['github_url']=student_data_row.github_url
			edit='<a href="'+str(request.scheme+'://'+request.get_host()+'/edit_student_profile/')+'">edit your profile</a>'
			JSON_response['edit']=edit
		else:
			print login_id

			JSON_response['login_id']=login_id
			student_data_row=student_data.objects.get(roll_no=roll_no)
			JSON_response['name']=student_data_row.name
			JSON_response['mobile']=student_data_row.mobile
			JSON_response['email']=student_data_row.email
			JSON_response['sem']=student_data_row.sem
			photo=str(student_data_row.photo)
			photo_url='<img src='+'"/media/'+photo+'"'+'>'
			JSON_response['photo']=photo_url
			print photo_url
			JSON_response['skill']=student_data_row.skill
			JSON_response['linkedin_url']=student_data_row.linkedin_url
			JSON_response['github_url']=student_data_row.github_url
		print JSON_response
		return render(request,'show_profile.html',JSON_response)
	except:
		return HttpResponse("failed")



# Create your views here.

from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import os

@csrf_exempt
def signup_faculty(request):
	if request.user.is_authenticated():
		return render (request,'welcome.html')
	else:
		if request.method=="POST":
			try:
				response={}
				login_id=str(request.POST.get('roll_no'))
				designation=str(request.POST.get('designation'))
				education=str(request.POST.get('education'))
				area_of_interest=str(request.POST.get('linkedin_url'))
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
				other_details=str(request.POST.get('skill'))
				password=str(request.POST.get('password'))
				try:
					faculty_data_row=faculty_data.objects.get(faculty_id=login_id)
					setattr(faculty_data_row,'designation',str(designation))
					setattr(faculty_data_row,'education',str(education))
					setattr(faculty_data_row,'area_of_interest',str(area_of_interest))
					setattr(faculty_data_row,'other_details',str(other_details))
					#image pending
					faculty_data_row.save()
					User.objects.create_user(username=login_id,password=password)
				except:
					return HttpResponse('Invalid login id')
			except:
				return HttpResponse("Data not get")
		else:
			return render(request,'signup_student.html')


@login_required
def faculty_profile(request,faculty_id):
	try:
		JSON_response={}
		login_id=str(request.user)
		if login_id==faculty_id:
			JSON_response['login_id']=login_id
			faculty_data_row=faculty_data.objects.get(faculty_id=faculty_id)
			JSON_response['name']=faculty_data_row.name
			JSON_response['mobile']=faculty_data_row.mobile
			JSON_response['email']=faculty_data_row.email
			JSON_response['designation']=faculty_data_row.designation
			photo=str(faculty_data_row.photo)
			photo_url='<img src='+'"/media/'+photo+'"'+'>'
			JSON_response['photo']=photo_url
			print photo_url
			JSON_response['education']=faculty_data_row.education
			JSON_response['area_of_interest']=faculty_data_row.area_of_interest
			JSON_response['other_details']=faculty_data_row.other_details
			edit='<a href="'+str(request.scheme+'://'+request.get_host()+'/edit_faculty_profile/')+'">edit your profile</a>'
			JSON_response['edit']=edit
		else:
			print login_id
			faculty_data_row=faculty_data.objects.get(faculty_id=faculty_id)
			JSON_response['login_id']=faculty_id
			JSON_response['name']=faculty_data_row.name
			JSON_response['mobile']=faculty_data_row.mobile
			JSON_response['email']=faculty_data_row.email
			JSON_response['designation']=faculty_data_row.designation
			photo=str(faculty_data_row.photo)
			photo_url='<img src='+'"/media/'+photo+'"'+'>'
			JSON_response['photo']=photo_url
			print photo_url
			JSON_response['education']=faculty_data_row.education
			JSON_response['area_of_interest']=faculty_data_row.area_of_interest
			JSON_response['other_details']=faculty_data_row.other_details
		print JSON_response
		return render(request,'show_faculty_profile.html',JSON_response)
	except:
		return HttpResponse("failed")


@login_required
def faculty_group_profile(request):
	try:
		for o in faculty_data.objects.all():
			return HttpResponse('whole faculty data will be passed at once')
	except:
		return HttpResponse('something occur please try again')



# Create your views here.


# Create your views here.

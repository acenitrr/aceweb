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
				login_id=str(request.POST.get('faculty_id'))
				designation=str(request.POST.get('designation'))
				print designation
				education=str(request.POST.get('education'))
				area_of_interest=str(request.POST.get('area_of_interest'))
				image_name=request.FILES.get('photo').name
				try:
					folder = 'media/faculty_images/'
					os.mkdir(os.path.join(folder))
				except Exception,e:
					print e
					pass
				print "image=",image_name
				url=folder+login_id+image_name
				fout = open(url, 'wb+')
				file_content = request.FILES.get('photo').read()
				fout.write(file_content)
				fout.close()
				other_details=str(request.POST.get('other_details'))
				print other_details
				password=str(request.POST.get('password'))
				print password
				try:
					faculty_data_row=faculty_data.objects.get(faculty_id=login_id)
					setattr(faculty_data_row,'designation',str(designation))
					setattr(faculty_data_row,'education',str(education))
					setattr(faculty_data_row,'area_of_interest',str(area_of_interest))
					setattr(faculty_data_row,'other_details',str(other_details))
					setattr(faculty_data_row,'photo',url)
					faculty_data_row.save()
					User.objects.create_user(username=login_id,password=password)
					return render(request,'login.html',{'msg':'Sign up done'})
				except Exception,e:
					print e
					return HttpResponse('Invalid login id')
			except:
				return HttpResponse("Data not get")


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
			photo_url='<img src='+'"/'+photo+'"'+'>'
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


@login_required
@csrf_exempt
def edit_faculty_profile(request):
	if request.method=='POST':
		try:
			faculty_data_row=faculty_data.objects.get(faculty_id=str(request.user))
			education=str(request.POST.get('education'))
			print education
			designation=str(request.POST.get('designation'))
			area_of_interest=str(request.POST.get('area_of_interest'))
			other_details=str(request.POST.get('other_details'))
			try:
				image_name=request.FILES.get('photo').name
				try:
					folder = 'media/faculty_images/'
					os.mkdir(os.path.join(folder))
				except Exception,e:
					print e
					pass
				print "image=",image_name
				url=folder+faculty_data_row.faculty_id+image_name
				fout = open(url, 'wb+')
				file_content = request.FILES.get('photo').read()
				fout.write(file_content)
				fout.close()
				setattr(faculty_data_row,'photo',url)
			except:
				pass
			setattr(faculty_data_row,'education',education)
			setattr(faculty_data_row,'designation',designation)
			setattr(faculty_data_row,'area_of_interest',area_of_interest)
			setattr(faculty_data_row,'other_details',other_details)
			#resume pending
			faculty_data_row.save()
			return HttpResponse('redirect him to his own profile')
		except:
			return HttpResponse('something occur please try again')
	else:
		faculty_data_row=faculty_data.objects.get(faculty_id=str(request.user))
		JSON_response={}
		JSON_response['faculty_id']=faculty_data_row.faculty_id
		JSON_response['name']=faculty_data_row.name
		JSON_response['mobile']=faculty_data_row.mobile
		JSON_response['email']=faculty_data_row.email
		JSON_response['designation']=faculty_data_row.designation
		photo=str(faculty_data_row.photo)
		photo_url='<img src='+'"/'+photo+'"'+'>'
		JSON_response['photo']=photo_url
		print photo_url
		JSON_response['education']=faculty_data_row.education
		JSON_response['area_of_interest']=faculty_data_row.area_of_interest
		JSON_response['other_details']=faculty_data_row.other_details
		return render (request,'edit_faculty_profile.html',JSON_response)



# Create your views here.


# Create your views here.

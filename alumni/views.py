from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import os

@csrf_exempt
def signup_new_alumni(request):
	if request.user.is_authenticated():
		return render (request,'welcome.html')
	else:
		if request.method=="POST":
			try:
				response={}
				login_id=str(request.POST.get('roll_no'))
				current_status=str(request.POST.get('current_status'))
				batch=str(request.POST.get('batch'))
				company_institue=str(request.POST.get('company_institue'))
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
				designation=str(request.POST.get('designation'))
				other=str(request.POST.get('other'))
				password=str(request.POST.get('password'))
				try:
					alumni_data_row=alumni_data.objects.get(roll_no=login_id)
					setattr(alumni_data_row,'current_status',str(current_status))
					setattr(alumni_data_row,'github_url',str(github_url))
					setattr(alumni_data_row,'linkedin_url',str(linkedin_url))
					setattr(alumni_data_row,'batch',str(batch))
					setattr(alumni_data_row,'company_institue',str(company_institue))
					setattr(alumni_data_row,'designation',str(designation))
					setattr(alumni_data_row,'other',str(other))
					setattr(alumni_data_row,'flag',True)
					#image pending
					alumni_data_row.save()
					User.objects.create_user(username=login_id,password=password)
				except:
					return HttpResponse('Invalid login id')
			except:
				return HttpResponse("Data not get")
		else:
			return render(request,'signup_alumni1.html')

@csrf_exempt
def signup_alumni(request):
	if request.user.is_authenticated():
		return render (request,'welcome.html')
	else:
		if request.method=="POST":
			try:
				response={}
				login_id=str(request.POST.get('roll_no'))
				current_status=str(request.POST.get('current_status'))
				batch=str(request.POST.get('batch'))
				company_institue=str(request.POST.get('company_institue'))
				designation=str(request.POST.get('designation'))
				other=str(request.POST.get('other'))
				try:
					alumni_data_row=alumni_data.objects.get(roll_no=login_id)
					setattr(alumni_data_row,'current_status',str(current_status))
					setattr(alumni_data_row,'github_url',str(github_url))
					setattr(alumni_data_row,'linkedin_url',str(linkedin_url))
					setattr(alumni_data_row,'batch',str(batch))
					setattr(alumni_data_row,'company_institue',str(company_institue))
					setattr(alumni_data_row,'designation',str(designation))
					setattr(alumni_data_row,'other',str(other))
					setattr(alumni_data_row,'flag',True)
					#image pending
					alumni_data_row.save()
				except:
					return HttpResponse('Invalid login id')
			except:
				return HttpResponse("Data not get")
		else:
			return render(request,'signup_alumni1.html')


@login_required
def alumni_profile(request,roll_no):
	try:
		JSON_response={}
		login_id=str(request.user)
		if login_id==roll_no:
			JSON_response['login_id']=login_id
			alumni_data_row=alumni_data.objects.get(roll_no=roll_no)
			JSON_response['name']=alumni_data_row.name
			JSON_response['mobile']=alumni_data_row.mobile
			JSON_response['email']=alumni_data_row.email
			JSON_response['batch']=alumni_data_row.batch
			photo=str(alumni_data_row.photo)
			photo_url='<img src='+'"/media/'+photo+'"'+'>'
			JSON_response['photo']=photo_url
			print photo_url
			JSON_response['current_status']=alumni_data_row.current_status
			JSON_response['linkedin_url']=alumni_data_row.linkedin_url
			JSON_response['github_url']=alumni_data_row.github_url
			JSON_response['company_institue']=alumni_data_row.company_institue
			JSON_response['designation']=alumni_data_row.designation
			JSON_response['skill']=alumni_data_row.skill
			JSON_response['other']=alumni_data_row.other
			edit='<a href="'+str(request.scheme+'://'+request.get_host()+'/edit_alumni_profile/')+'">edit your profile</a>'
			JSON_response['edit']=edit
		else:
			print login_id
			JSON_response['login_id']=roll_no
			alumni_data_row=alumni_data.objects.get(roll_no=roll_no)
			JSON_response['name']=alumni_data_row.name
			JSON_response['mobile']=alumni_data_row.mobile
			JSON_response['email']=alumni_data_row.email
			JSON_response['batch']=alumni_data_row.batch
			photo=str(alumni_data_row.photo)
			photo_url='<img src='+'"/media/'+photo+'"'+'>'
			JSON_response['photo']=photo_url
			print photo_url
			JSON_response['current_status']=alumni_data_row.current_status
			JSON_response['linkedin_url']=alumni_data_row.linkedin_url
			JSON_response['github_url']=alumni_data_row.github_url
			JSON_response['company_institue']=alumni_data_row.company_institue
			JSON_response['designation']=alumni_data_row.designation
			JSON_response['skill']=alumni_data_row.skill
			JSON_response['other']=alumni_data_row.other
		print JSON_response
		return render(request,'show_profile.html',JSON_response)
	except:
		return HttpResponse("Wrong roll_no entered")


@login_required
def alumni_group_profile(request):
	try:
		key=str(request.GET.get('key'))
		value=str(request.GET.get('value'))
		if(key=='roll_no'):
			link='/alumni_view/'+value
			return HttpResponseRedirect(str(link))
		else:
			if key=='name':
				count = alumni_data.objects.filter(name=value).count()
				if count==0:
					return render(request,'profile.html',{'msg':'no profile found for such name'})
				else:
					for o in alumni_data.objects.filter(name=value):
						return HttpResponse('profile html code will be passed as context in render')
			else:
				if key=='batch':
					count = alumni_data.objects.filter(batch=value).count()
					if count==0:
						return render(request,'profile.html',{'msg':'please enter correct batch'})
					else:
						for o in alumni_data.objects.filter(batch=value):
							return HttpResponse('profile html code will be passed as context in render')
				else:
					return HttpResponse('please choose field from give list')
	except:
		return HttpResponse('something occur please try again')


			



# Create your views here.

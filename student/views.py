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
		return render (request,'index.html',{'link2':'<a href="/logout/">LOGOUT</a>'})
	else:
		if request.method=="POST":
			try:
				response={}
				login_id=str(request.POST.get('roll_no'))
				print login_id
				sem=str(request.POST.get('sem'))
				print sem
				github_url=str(request.POST.get('github_url'))
				linkedin_url=str(request.POST.get('linkedin_url'))
				image_name=request.FILES.get('photo').name
				try:
					folder = 'media/student_images/'
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
				skill=str(request.POST.get('skill'))
				print skill
				password=str(request.POST.get('password'))
				try:
					student_data_row=student_data.objects.get(roll_no=login_id)
					setattr(student_data_row,'sem',str(sem))
					setattr(student_data_row,'github_url',str(github_url))
					setattr(student_data_row,'linkedin_url',str(linkedin_url))
					setattr(student_data_row,'skill',str(skill))
					setattr(student_data_row,'photo',url)
					student_data_row.save()
					User.objects.create_user(username=login_id,password=password)
					return render(request,'login.html',{'msg':'sign up done'})
				except Exception,e:
					print e
					return render(request,'signup_student.html',{'msg':'Invalid login id'})
			except Exception,e:
				print e
				return render(request,'signup_student.html',{'msg':'Data not get'})
		return render (request,'signup_student.html')


@login_required
def student_profile(request,roll_no):
	try:
		JSON_response={}
		login_id=str(request.user)
		JSON_response['login_id']=roll_no
		student_data_row=student_data.objects.get(roll_no=roll_no)
		JSON_response['name']=student_data_row.name
		JSON_response['sem']=student_data_row.sem
		photo=str(student_data_row.photo)
		photo_url=' src='+'"/'+photo+'"'
		JSON_response['photo']=photo_url
		print photo_url
		JSON_response['skill']=student_data_row.skill
		JSON_response['linkedin_url']=student_data_row.linkedin_url
		JSON_response['github_url']=student_data_row.github_url
		JSON_response['link2']='<a href="/logout/">LOGOUT</a>'
		if login_id==roll_no:
			edit_url=str(request.scheme+'://'+request.get_host()+'/edit_student_profile/')
			edit='<a href="'+edit_url+'"'+' class="btn btn-default" style="float:right">Edit</a>'
			JSON_response['edit']=edit
		else:
			ping='<a href="/ping/'+roll_no+'"'+ 'class="btn btn-default" style="float:right">Ping</a>'
			JSON_response['ping']=ping
		print JSON_response
		return render(request,'show_profile.html',JSON_response)
	except:
		return render(request,'show_profile.html',{'msg':'Wrong Data','link2':'<a href="/logout/">LOGOUT</a>'})

@csrf_exempt
@login_required
def student_group_profile(request):
	if request.method=='POST':
		try:
			key=str(request.POST.get('key'))
			value=str(request.POST.get('value'))
			print value
			print key
			if(key=='0'):
				link='/student_view/'+str(value)
				print link
				return HttpResponseRedirect(link)
			else:
				if key=='1':
					count = student_data.objects.filter(name__iexact=value).count()
					if count==0:
						return render(request,'search_profile.html',{'msg':'no profile found for such name','keyword':'Semester','link2':'<a href="/logout/">LOGOUT</a>'})
					else:
						stu_name_profile=''
						for o in student_data.objects.filter(name__iexact=value):
							stu_name_profile+="<tr><td><a href='/student_view/"+o.roll_no+"'>"+o.roll_no+"</a></td>"
							stu_name_profile+="<td>"+o.name+"</td>"
							stu_name_profile+="<td>"+str(o.sem)+"</td></tr>"
						return render(request,'profiletable.html',{'data':stu_name_profile,'key':'Semester','link2':'<a href="/logout/">LOGOUT</a>'})
				else:
					if key=='2':
						count = student_data.objects.filter(sem=value).count()
						if count==0:
							return render(request,'searchprofile.html',{'msg':'please enter correct semester','keyword':'Semester','link1':'<a href="/profile/">PROFILE</a>','link2':'<a href="/logout/">LOGOUT</a>'})
						else:
							stu_name_profile=''
							for o in student_data.objects.filter(sem=value):
								stu_name_profile+="<tr><td><a href='/student_view/"+o.roll_no+"'>"+o.roll_no+"</a></td>"
								stu_name_profile+="<td>"+o.name+"</td>"
								stu_name_profile+="<td>"+str(o.sem)+"</td></tr>"
							return render(request,'profiletable.html',{'data':stu_name_profile,'key':'Semester','link2':'<a href="/logout/">LOGOUT</a>'})
					else:
						return render(request,'search_profile.html',{'msg':'Invalid request','keyword':'Semester','link2':'<a href="/logout/">LOGOUT</a>'})
		except Exception,e:
			print e
			return HttpResponse('something occur please try again')
	else:
		return render(request,'search_profile.html',{'link2':'<a href="/logout/">LOGOUT</a>','keyword':'Semester'})


@login_required
@csrf_exempt
def edit_student_profile(request):
	if request.method=='POST':
		try:
			student_data_row=student_data.objects.get(roll_no=str(request.user))
			skill=str(request.POST.get('skill'))
			print skill
			linkedin_url=str(request.POST.get('linkedin_url'))
			github_url=str(request.POST.get('github_url'))
			print github_url
			try:
				image_name=request.FILES.get('photo').name
				try:
					folder = 'media/student_images/'
					os.mkdir(os.path.join(folder))
				except Exception,e:
					print e
					pass
				print "image=",image_name
				url=folder+student_data_row.roll_no+image_name
				fout = open(url, 'wb+')
				file_content = request.FILES.get('photo').read()
				fout.write(file_content)
				fout.close()
				setattr(student_data_row,'photo',url)
			except:
				pass
			setattr(student_data_row,'skill',skill)
			setattr(student_data_row,'linkedin_url',linkedin_url)
			setattr(student_data_row,'github_url',github_url)
			student_data_row.save()
			redirect_url='/student_view/'+str(request.user)
			return HttpResponseRedirect(redirect_url)
		except Exception,e:
			print e
			return render (request,'edit_student_profile.html',{'msg':'something occur please try again','link1':'<a href="/profile/">PROFILE</a>','link2':'<a href="/logout/">LOGOUT</a>'})
	else:
		student_data_row=student_data.objects.get(roll_no=str(request.user))
		JSON_response={}
		JSON_response['roll_no']=student_data_row.roll_no
		JSON_response['name']=student_data_row.name
		JSON_response['mobile']=student_data_row.mobile
		JSON_response['email']=student_data_row.email
		JSON_response['sem']=student_data_row.sem

		photo_url='<img width="80" height="80" src='+'"/'+str(student_data_row.photo)+'"'+'>'
		JSON_response['photo']=photo_url
		print photo_url
		JSON_response['photo_name']=str(student_data_row.photo)
		JSON_response['skill']=student_data_row.skill
		JSON_response['linkedin_url']=student_data_row.linkedin_url
		JSON_response['github_url']=student_data_row.github_url
		JSON_response['link2']='<a href="/logout/">LOGOUT</a>'
		return render (request,'edit_student_profile.html',JSON_response)


from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

@csrf_exempt
def signup_alumni(request):
	if request.user.is_authenticated():
		return render (request,'index.html',{'link2':'<a href="/logout/">LOGOUT</a>'})
	else:
		if request.method=="POST":
			try:
				response={}
				login_id=str(request.POST.get('roll_no'))
				current_status=str(request.POST.get('current_status'))
				batch=str(request.POST.get('batch'))
				company_institue=str(request.POST.get('company_institue'))
				github_url=str(request.POST.get('github_url'))
				linkedin_url=str(request.POST.get('linkedin_url'))
				print 21
				image_name=request.FILES.get('photo').name
				try:
					folder = 'media/alumni_images/'
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
				designation=str(request.POST.get('designation'))
				other=str(request.POST.get('other'))
				password=str(request.POST.get('password'))
				print password
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
					setattr(alumni_data_row,'photo',url)
					#image pending
					alumni_data_row.save()
					User.objects.create_user(username=login_id,password=password)
					return render(request,'login.html',{'msg':'sign up done','link2':'<a href="/login/">LOGIN</a>'})
				except Exception,e:
					print e
					return render(request,'login.html',{'msg':'Invalid login id','link2':'<a href="/login/">LOGIN</a>'})
			except Exception,e:
				print e
				return render(request,'login.html',{'msg':'Data not get','link2':'<a href="/login/">LOGIN</a>'})
		else:
			return render(request,'signup_alumni.html',{'link2':'<a href="/login/">LOGIN</a>'})

# @csrf_exempt
# def signup_alumni(request):
# 	if request.user.is_authenticated():
# 		return render (request,'welcome.html')
# 	else:
# 		if request.method=="POST":
# 			try:
# 				response={}
# 				login_id=str(request.POST.get('roll_no'))
# 				current_status=str(request.POST.get('current_status'))
# 				batch=str(request.POST.get('batch'))
# 				company_institue=str(request.POST.get('company_institue'))
# 				designation=str(request.POST.get('designation'))
# 				other=str(request.POST.get('other'))
# 				try:
# 					alumni_data_row=alumni_data.objects.get(roll_no=login_id)
# 					setattr(alumni_data_row,'current_status',str(current_status))
# 					setattr(alumni_data_row,'github_url',str(github_url))
# 					setattr(alumni_data_row,'linkedin_url',str(linkedin_url))
# 					setattr(alumni_data_row,'batch',str(batch))
# 					setattr(alumni_data_row,'company_institue',str(company_institue))
# 					setattr(alumni_data_row,'designation',str(designation))
# 					setattr(alumni_data_row,'other',str(other))
# 					setattr(alumni_data_row,'flag',True)
# 					#image pending
# 					alumni_data_row.save()
# 				except:
# 					return HttpResponse('Invalid login id')
# 			except:
# 				return HttpResponse("Data not get")
# 		else:
# 			return render(request,'signup_alumni.html')


@login_required
def alumni_profile(request,roll_no):
	try:
		JSON_response={}
		login_id=str(request.user)
		if login_id==roll_no:
			JSON_response['login_id']=login_id
			alumni_data_row=alumni_data.objects.get(roll_no=roll_no)
			JSON_response['name']=alumni_data_row.name
			JSON_response['batch']=alumni_data_row.batch
			photo=str(alumni_data_row.photo)
			photo_url=' src='+'"/'+photo+'"'
			JSON_response['photo']=photo_url
			print photo_url
			JSON_response['current_status']=alumni_data_row.current_status
			JSON_response['linkedin_url']=alumni_data_row.linkedin_url
			JSON_response['github_url']=alumni_data_row.github_url
			JSON_response['company_institue']=alumni_data_row.company_institue
			JSON_response['designation']=alumni_data_row.designation
			JSON_response['other']=alumni_data_row.other
			JSON_response['link2']='<a href="/logout/">LOGOUT</a>'
			edit_url=str(request.scheme+'://'+request.get_host()+'/edit_alumni_profile/')
			edit='<a href="'+edit_url+'"'+' class="btn btn-default" style="float:right">Edit</a>'
			JSON_response['edit']=edit
		else:
			print login_id
			JSON_response['login_id']=roll_no
			alumni_data_row=alumni_data.objects.get(roll_no=roll_no)
			JSON_response['name']=alumni_data_row.name
			JSON_response['batch']=alumni_data_row.batch
			photo=str(alumni_data_row.photo)
			photo_url=' src='+'"/'+photo+'"'
			JSON_response['photo']=photo_url
			print photo_url
			JSON_response['current_status']=alumni_data_row.current_status
			JSON_response['linkedin_url']=alumni_data_row.linkedin_url
			JSON_response['github_url']=alumni_data_row.github_url
			JSON_response['company_institue']=alumni_data_row.company_institue
			JSON_response['designation']=alumni_data_row.designation
			JSON_response['other']=alumni_data_row.other
			JSON_response['link2']='<a href="/logout/">LOGOUT</a>'
			ping='<a href="/ping/'+roll_no+'"'+ 'class="btn btn-default" style="float:right">Ping</a>'
			# ping='<a href="'+'/ping/'+roll_no+'"'+'>Contact</a>'
			JSON_response['ping']=ping
		print JSON_response
		return render(request,'show_alumni_profile.html',JSON_response)
	except:
		return render(request,'show_alumni_profile.html',{'msg':'Wrong roll_no entered'})
@csrf_exempt
@login_required
def alumni_group_profile(request):
	if request.method=="POST":
		try:
			key=str(request.POST.get('key'))
			value=str(request.POST.get('value'))
			if(key=='0'):
				link='/alumni_view/'+str(value)
				print link
				return HttpResponseRedirect(link)
			else:
				if key=='1':
					count = alumni_data.objects.filter(name__iexact=value).count()
					if count==0:
						return render(request,'search_profile.html',{'msg':'no profile found for such name','keyword':'Batch','link2':'<a href="/logout/">LOGOUT</a>'})
					else:
						alu_name_profile=''
						for o in alumni_data.objects.filter(name__iexact=value):
							alu_name_profile+="<tr><td><a href='/alumni_view/"+o.roll_no+"'>"+o.roll_no+"</a></td>"
							alu_name_profile+="<td>"+o.name+"</td>"
							alu_name_profile+="<td>"+str(o.batch)+"</td></tr>"
						return render(request,'profiletable.html',{'data':alu_name_profile,'key':'Batch','link2':'<a href="/logout/">LOGOUT</a>'})
				else:
					if key=='2':
						count = alumni_data.objects.filter(batch=value).count()
						if count==0:
							return render(request,'search_profile.html',{'msg':'no profile found for such name', 'keyword':'Batch','link2':'<a href="/logout/">LOGOUT</a>'})
						else:
							alu_name_profile=''
							for o in alumni_data.objects.filter(batch=value):
								alu_name_profile+="<tr><td><a href='/alumni_view/"+o.roll_no+"'>"+o.roll_no+"</a></td>"
								alu_name_profile+="<td>"+o.name+"</td>"
								alu_name_profile+="<td>"+str(o.batch)+"</td></tr>"
							return render(request,'profiletable.html',{'data':alu_name_profile,'key':'Batch','link2':'<a href="/logout/">LOGOUT</a>'})
					else:
						return render(request,'search_profile.html',{'msg':'Invalid request','keyword':'Batch','link2':'<a href="/logout/">LOGOUT</a>'})
		except Exception,e:
			print e
			return HttpResponse('something occur please try again')
	else:
		return render(request,'search_profile.html',{'link2':'<a href="/logout/">LOGOUT</a>','keyword':'Batch'})



@login_required
@csrf_exempt
def edit_alumni_profile(request):
	if request.method=='POST':
		try:
			alumni_data_row=alumni_data.objects.get(roll_no=str(request.user))
			current_status=str(request.POST.get('current_status'))
			company_institue=str(request.POST.get('company_institue'))
			designation=str(request.POST.get('designation'))
			skill=str(request.POST.get('skill'))
			other=str(request.POST.get('other'))
			linkedin_url=str(request.POST.get('linkedin_url'))
			github_url=str(request.POST.get('github_url'))
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
			setattr(alumni_data_row,'current_status',current_status)
			setattr(alumni_data_row,'company_institue',company_institue)
			setattr(alumni_data_row,'designation',designation)
			setattr(alumni_data_row,'skill',skill)
			setattr(alumni_data_row,'other',other)
			setattr(alumni_data_row,'linkedin_url',linkedin_url)
			setattr(alumni_data_row,'github_url',github_url)
			#image pending
			alumni_data_row.save()
			redirect_url='/alumni_view/'+str(request.user)
			return HttpResponseRedirect(redirect_url)
		except:
			link1='<div class="dropdown"><button class="dropbtn">PROFILE</button><div class="dropdown-content">'
			link1+='<a href="/student_view/'+str(request.user)+'" >MY PROFILE</a>'
			link1+='<a href="/students_profile">STUDENTS</a><a href="/alumni_profile">ALUMNI</a></div></div>'
			return render (request,'edit_alumni_profile.html',{'msg':'something occur please try again','link1':link1,'link2':'<a href="/login/">LOGIN</a>'})
	else:
		alumni_data_row=alumni_data.objects.get(roll_no=str(request.user))
		JSON_response={}
		JSON_response['roll_no']=alumni_data_row.roll_no
		JSON_response['name']=alumni_data_row.name
		JSON_response['mobile']=alumni_data_row.mobile
		JSON_response['email']=alumni_data_row.email
		JSON_response['batch']=alumni_data_row.batch
		photo=str(alumni_data_row.photo)
		photo_url='<img src='+'"/'+photo+'"'+'>'
		JSON_response['photo']=photo_url
		print photo_url
		JSON_response['current_status']=alumni_data_row.current_status
		JSON_response['linkedin_url']=alumni_data_row.linkedin_url
		JSON_response['github_url']=alumni_data_row.github_url
		JSON_response['company_institue']=alumni_data_row.company_institue
		JSON_response['designation']=alumni_data_row.designation
		JSON_response['skill']=alumni_data_row.skill
		JSON_response['other']=alumni_data_row.other
		JSON_response['link2']='<a href="/logout/">LOGOUT</a>'
		return render (request,'edit_alumni_profile.html',JSON_response)

# Create your views here.
@csrf_exempt
def whatsapp(request):
	if request.method == 'GET' :
		print "0"
		driver = webdriver.Chrome('/home/arpit/Downloads/chromedriver')
		print "1"
		driver.get("https://web.whatsapp.com/")
		print "2"
		wait = WebDriverWait(driver, 120)
		print "3"
		# Replace 'Friend's Name' with the name of your friend 
		# or the name of a group 
		array = ['"Arpit Jain"','"Aditya Agrawal"']
		for i in array:
			target = i
			print "21"
			 
			# Replace the below string with your own message
			string = "testing"
			print "25"
			 
			x_arg = '//span[contains(@title,' + target + ')]'
			print x_arg
			try:
				group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
				group_title.click()
			except Exception as e:
				print str(e) + "group click"

			try:
				inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
			except Exception as e :
				print str(e) + "inp"	

			try:
				input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
			except Exception as e:
				print str(e)+ "input _box"

			try:
				for i in range(2):
				    input_box.send_keys(string + Keys.ENTER)
				    # time.sleep(1)
			except Exception as e:
				raise
		return HttpResponse("Ok")		
@csrf_exempt
def whatsapp1(request):
	if request.method == 'GET' :
		print "0"
		driver = webdriver.Chrome('/home/arpit/Downloads/chromedriver')
		print "1"
		driver.get("https://web.whatsapp.com/")
		print "2"
		wait = WebDriverWait(driver, 120)
		print "3"
		# Replace 'Friend's Name' with the name of your friend 
		# or the name of a group 
		target = '"Aaditya Nit"'
		print "21"
		 
		# Replace the below string with your own message
		string = "Aditya Chutiya hai!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
		print "25"
		 
		x_arg = '//span[contains(@title,' + target + ')]'
		print x_arg
		try:
			group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
			group_title.click()
		except Exception as e:
			print str(e) + "group click"

		try:
			inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
		except Exception as e :
			print str(e) + "inp"	

		try:
			input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
		except Exception as e:
			print str(e)+ "input _box"

		try:
			for i in range(1000):
			    input_box.send_keys(string + Keys.ENTER)
			    time.sleep(1)
		except Exception as e:
			raise
		return HttpResponse("Ok")
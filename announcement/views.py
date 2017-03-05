from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from login.models import *
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse



# def get_announcement(request):
# 	response={}
# 	json_list=[]
# 	for o in announcement_data.objects.all():
# 		if(o.active==True):
# 			tmp_json={}
# 			tmp_json['title']=o.title
# 			tmp_json['subtitle']=o.title
# 			tmp_json['content']=o.content
# 			tmp_json['created']=o.created
# 			json_list.append(tmp_json)
	
# 	response['list']=json_list
# 	return JsonResponse(response)

def announcement(request):
	# try:
	announcement_string=''
	for o in announcement_data.objects.all().order_by('title'):
		if(o.active==True):
			announcement_temp_string="""
			<li>
					<time class="cbp_tmtime" datetime="2017-25-02 11:00">
					<span style="color:black;"><b></b></span> 
					<span STYLE="FONT-SIZE:20PX;color:#1c2d3f">%s</span></time>
					<div class="cbp_tmicon cbp_tmicon-screen"></div>
					<div class="cbp_tmlabel" style="background:#1c2d3f;">
						<h2>%s</h2>
						<p >%s</p>
					</div>
				</li>"""
			announcement_string+=announcement_temp_string % (o.title,o.subtitle,o.content)	
	return render(request,'activities.html' ,{'announcement_string':announcement_string})
	# except:
	# 	return render(request,'activities.html' ,{'announcement_string':'No upcoming activities'})


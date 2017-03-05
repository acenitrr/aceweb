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
# 			tmp_json['content']=o.content
# 			tmp_json['issuer']=o.issuer
# 			tmp_json['file']=o.file
# 			tmp_json['date_issued']=o.date_issued
# 			tmp_json['created']=o.created
# 			json_list.append(tmp_json)
# 			response.append(json_list)

# 	return JsonResponse(response)

def announcement(request):
	# try:
	announcement_string=''
	flag=0
	temp_obj={}
	for o in announcement_data.objects.all().order_by('title'):
		if(o.active==True):
			if flag==0:
				announcement_temp_string="""<li>
					<time class="cbp_tmtime" datetime="2017-25-02 11:00">
					<span style="color:black;"><b></b></span> 
					<span STYLE="FONT-SIZE:20PX;color:#1c2d3f">%s</span></time>
					<div class="cbp_tmicon cbp_tmicon-screen"></div>
					<div class="cbp_tmlabel" style="background:#1c2d3f;">
                             <div class="container-fluid">
                    <div class="row">
                    <div class="col-sm-12">
                    <p><h2>%s</h2>
                            <p style="padding-right:10px;" >%s</p></p>
                    </div></div></div>		
						</div>"""
				flag=1	
				temp_obj=o
				announcement_string+=announcement_temp_string % (o.title,o.subtitle,o.content)
			else:
				if  o.title==temp_obj.title:
					announcement_temp_string="""<div class="cbp_tmlabel" style="background:#1c2d3f;">
		                             <div class="container-fluid">
		                    <div class="row">
		                    <div class="col-sm-12">
		                    <p><h2>%s</h2>
		                            <p style="padding-right:10px;" >%s</p></p>
		                    </div></div></div>		
								</div>"""
					announcement_string+=announcement_temp_string % (o.subtitle,o.content)
				else:
					announcement_temp_string="""</ul><ul class="cbp_tmtimeline"><li>
						<time class="cbp_tmtime" datetime="2017-25-02 11:00">
						<span style="color:black;"><b></b></span> 
						<span STYLE="FONT-SIZE:20PX;color:#1c2d3f">%s</span></time>
						<div class="cbp_tmicon cbp_tmicon-screen"></div>
						<div class="cbp_tmlabel" style="background:#1c2d3f;">
	                             <div class="container-fluid">
	                    <div class="row">
	                    <div class="col-sm-12">
	                    <p><h2>%s</h2>
	                            <p style="padding-right:10px;" >%s</p></p>
	                    </div></div></div>		
							</div>"""
					announcement_string+=announcement_temp_string % (o.title,o.subtitle,o.content)
					temp_obj=o
	return render(request,'activities.html' ,{'announcement_string':announcement_string})
	# except:
	# 	return render(request,'activities.html' ,{'announcement_string':'No upcoming activities'})

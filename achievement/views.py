from django.shortcuts import render

# Create your views here.
from .models import *
 


 # training_placement_achievement_data


 # academics_achievement_data


 # cocurricular_achievement_data

def achievements(request):
	data1=''
	data2=''
	data3='<style>'
	c1="#1c2d3f"
	c2="#cc0019"
	i=0
	try:
		for o in overall_achievement_data.objects.all():
			i+=1
			if(i%2==0):
				data1+='<div class="cube" data-bg-color="'+c1+'" data-title="'+o.title+'"></div>'
			else:
				data1+='<div class="cube" data-bg-color="'+c2+'" data-title="'+o.title+'"></div>'

			data2+="""<div class="content__block">
						<h3 class="content__title" style="position:absolute;top:20px;">"""+o.title+"""</h3>
						<p style="position:absolute;top:100px;font-size:25px;"><b>"""+o.description+"""</b></p>
					</div>"""
			data3+=""".cube:not(.cube--inactive):nth-child("""+str(i)+""") .cube__side,
			.no-js .cube:not(.cube--inactive):nth-child("""+str(i)+""") {	background-image: url(/media/"""+str(o.photo)+""");}"""
	except Exception,e:
		data=e
		print e
	if request.user.is_authenticated():
		return render(request,'achievements.html' ,{'datahead':data3+'</style>','data1':data1,'data2':data2,'link1':'<a href="/profile/">PROFILE</a>','link2':'<a href="/logout/">LOGOUT</a>'})
	else:
		return render(request,'achievements.html',{'datahead':data3+'</style>','data1':data1,'data2':data2,'link2':'<a href="/login/">LOGIN</a>'})
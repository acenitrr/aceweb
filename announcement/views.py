from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from login.models import *
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponse



@csrf_exempt
@login_required
def add_announcement(request):
	login_id=str(request.user)
	login_row=login_data.objects.get(login_id=login_id)
	group_id=login_row.group_id
	if group_id==4:
		if request.method=='POST':
			title=str(request.POST.get('title'))
			content=str(request.POST.get('content'))
			issuer=str(login_id)
			# file pending
			# active ko idr se use krna hai ya fhir admin panel
			date_issued=str(datetime.datetime.now())
			announcement_data.objects.create(
				title=title,
				content=content,
				issuer=issuer,
				date_issued=date_issued
				)
			return render(request,'add_announcement.html',{'msg':'announcement_data is added makeit active through admin panel'})
		else:
			return render(request,'add_announcement.html')
	else:
		return HttpResponse('404 not found')


# Create your views here.

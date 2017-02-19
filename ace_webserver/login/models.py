from __future__ import unicode_literals

from django.db import models

class login_data(models.Model):
	login_id=models.CharField(primary_key=True,max_length=120,blank=False,null=False)
	group_id=models.CharField(max_length=120,blank=False,null=False)
	password=models.CharField(max_length=120,blank=True,null=True)
	otp= models.CharField(max_length=10,blank=True,null=True)
	email=models.CharField(max_length=200,blank=True,null=True)
	email_flag=models.BooleanField(default=False)
	content_flag=models.BooleanField(default=False)

# Create your models here.

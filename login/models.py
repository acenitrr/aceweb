from __future__ import unicode_literals

from django.db import models

class login_data(models.Model):
	login_id=models.CharField(primary_key=True,max_length=120,blank=False,null=False)
	group_choices=(
		(1,'student'),
		(2,'faculty'),
		(3,'alumni'),
		(4,'admin'),
		(5,'developer'),
		)
	group_id=models.IntegerField(choices=group_choices,default=0)
	password=models.CharField(max_length=120,blank=True,null=True)
	email=models.CharField(max_length=200,blank=True,null=True)
	email_flag=models.BooleanField(default=False)

# Create your models here.

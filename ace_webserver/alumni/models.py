from __future__ import unicode_literals

from django.db import models

class alumni_data(models.Model):
	enroll_no=models.CharField(primary_key=True,max_length=20,blank=False,null=False)
	name=models.CharField(max_length=200,blank=True,null=True)
	mobile=models.CharField(max_length=20,blank=True,null=True)
	# current_status=(
	# 	("1","pursuing further study"),
	# 	("2","Doing job"),
	# 	("3","other"),
	# 	)
	current_status=models.CharField(max_length=300,blank=True,null=True)
	company_institue=models.CharField(max_length=300,blank=True,null=True)
	designation=models.CharField(max_length=300,blank=True,null=True)
	email=models.CharField(max_length=300,blank=True,null=True)
	other=models.TextField(blank=True,null=True)

# Create your models here.

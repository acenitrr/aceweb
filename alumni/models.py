from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

class alumni_data(models.Model):
	roll_no=models.CharField(primary_key=True,max_length=20,blank=False,null=False)
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
	other=HTMLField()
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
	photo=models.ImageField(upload_to="faculty_images/",default="default.png")
# Create your models here.

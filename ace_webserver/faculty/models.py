from __future__ import unicode_literals
from tinymce.models import HTMLField

from django.db import models

class faculty_data(models.Model):
	faculty_id=models.CharField(primary_key=True,max_length=20,blank=False,null=False)
	name=models.CharField(max_length=300,blank=True,null=True)
	# designation_choice=(
	# 	("Professor","Professor"),
	# 	("Assistant Professor","Assistant Professor"),
	# 	("Temporary Faculty","Temporary Faculty"),
	# 	)
	designation=models.CharField(max_length=200,blank=True,null=True)
	# designation=models.CharField(choices=designation_choice,max_length=200,blank=True,null=True)
	education=models.CharField(max_length=300,blank=True,null=True)
	email=models.CharField(max_length=300,blank=True,null=True)
	mobile=models.CharField(max_length=20,blank=True,null=True)
	photo=models.ImageField(upload_to="faculty_images/",default="media/default.png")

class area_of_interest_data(models.Model):
	faculty_id=models.SmallIntegerField(primary_key=True)
	area_of_interest=models.CharField(max_length=300,blank=True,null=True)

class other_details_data(models.Model):
	faculty_id=models.SmallIntegerField(primary_key=True)
	other_details=HTMLField()

# Create your models here.

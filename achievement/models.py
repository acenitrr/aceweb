from __future__ import unicode_literals

from django.db import models

# Create your models here.
class overall_achievement_data(models.Model):
	photo=models.ImageField(upload_to="achievemnt_images/",default="default.png")
	title=models.CharField(max_length=120,blank=True,null=True)
	description=models.CharField(max_length=120,blank=True,null=True)

class training_placement_achievement_data(models.Model):
	photo=models.ImageField(upload_to="achievemnt_images/",default="default.png")
	title=models.CharField(max_length=120,blank=True,null=True)
	description=models.CharField(max_length=120,blank=True,null=True)

class academics_achievement_data(models.Model):
	photo=models.ImageField(upload_to="achievemnt_images/",default="default.png")
	title=models.CharField(max_length=120,blank=True,null=True)
	description=models.CharField(max_length=120,blank=True,null=True)

class cocurricular_achievement_data(models.Model):
	photo=models.ImageField(upload_to="achievemnt_images/",default="default.png")
	title=models.CharField(max_length=120,blank=True,null=True)
	description=models.CharField(max_length=120,blank=True,null=True)

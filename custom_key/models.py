from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

class custom_key_data(models.Model):
	key=models.CharField(max_length=300,blank=False,null=False)
	value=models.TextField()
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

class email_key_data(models.Model):
	key=models.CharField(max_length=300,blank=False,null=False)
	value=HTMLField()
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
# # Create your models here.

from __future__ import unicode_literals

from django.db import models

class keys_data(models.Model):
	host=models.CharField(max_length=300,blank=False,null=False)
	port=models.CharField(max_length=300,blank=False,null=False)
	username=models.CharField(max_length=300,blank=False,null=False)
	password=models.CharField(max_length=300,blank=False,null=False)
	flag=models.BooleanField(default=False)


# Create your models here.

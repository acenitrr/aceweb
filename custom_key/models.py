from __future__ import unicode_literals

from django.db import models

class custom_keys_data(models.Model):
	key=models.CharField(max_length=300,blank=False,null=False)
	value=models.CharField(max_length=300,blank=False,null=False)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

# class email_send_data(models.Model):
# 	key=models.CharField(max_length=300,blank=False,null=False)
# 	email_data=models.TextField()
# 	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
# 	created= models.DateTimeField(auto_now=False,auto_now_add=True)
# # Create your models here.

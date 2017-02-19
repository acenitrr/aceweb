from __future__ import unicode_literals

from django.db import models

class custom_keys_data(models.Model):
	key=models.CharField(max_length=300,blank=False,null=False)
	value=models.CharField(max_length=300,blank=False,null=False)

class email_send_data(models.Model):
	key=models.CharField(max_length=300,blank=False,null=False)
	email_data=models.TextField()

# Create your models here.

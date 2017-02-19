from __future__ import unicode_literals

from django.db import models

class internal_key_data(models.Model):
	key=models.CharField(max_length=200,blank=True,null=True)
	value=models.CharField(max_length=200,blank=True,null=True)

# Create your models here.

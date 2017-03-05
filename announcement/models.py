from __future__ import unicode_literals

from django.db import models

# Create your models here.
class announcement_title(models.Model):
	title=models.CharField(max_length=120,blank=True,null=True)
	def __unicode__(self):
		return self.title

class announcement_data(models.Model):
	title=models.ForeignKey(announcement_title,null=True)
	subtitle=models.CharField(max_length=120,blank=True,null=True)
	content=models.CharField(max_length=120,blank=True,null=True)
	issuer=models.CharField(max_length=120,blank=True,null=True)
	active=models.BooleanField(default=True)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)


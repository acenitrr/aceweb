from django.contrib import admin
from .models import *
# Register your models here.

class announcement_titleAdmin(admin.ModelAdmin):
	list_display=["title"]

admin.site.register(announcement_title,announcement_titleAdmin)

class announcement_dataAdmin(admin.ModelAdmin):
	list_display=["title",'subtitle',"issuer",'active','content']

admin.site.register(announcement_data,announcement_dataAdmin)

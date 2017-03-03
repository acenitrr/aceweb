from django.contrib import admin
from .models import *
# Register your models here.
class announcement_dataAdmin(admin.ModelAdmin):
	list_display=["title",'subtitle',"issuer","date_issued",'active','content','file']

admin.site.register(announcement_data,announcement_dataAdmin)

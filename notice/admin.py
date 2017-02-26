from django.contrib import admin
from .models import *
# Register your models here.
class notice_dataAdmin(admin.ModelAdmin):
	list_display=["title","issuer","date_issued",'active','file']

admin.site.register(notice_data,notice_dataAdmin)

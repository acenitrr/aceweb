from django.contrib import admin
from .models import *
# Register your models here.
class announcement_dataAdmin(admin.ModelAdmin):
	list_display=["title","issuer","date_issued"]

admin.site.register(announcement_data,announcement_dataAdmin)

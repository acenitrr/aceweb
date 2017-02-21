from django.contrib import admin
from .models import *

class custom_key_dataAdmin(admin.ModelAdmin):
	list_display=["key","value"]

admin.site.register(custom_key_data,custom_key_dataAdmin)

class email_send_dataAdmin(admin.ModelAdmin):
	list_display=["key","email_data"]

admin.site.register(email_send_data,email_send_dataAdmin)
# # Register your models here.

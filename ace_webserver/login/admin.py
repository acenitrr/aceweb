from django.contrib import admin
from .models import *

class login_dataAdmin(admin.ModelAdmin):
	list_display=["login_id","group_id","otp","email_flag","content_flag","email","password"]
	search_fields=["login_id","group_id"]

admin.site.register(login_data,login_dataAdmin)

# Register your models here.

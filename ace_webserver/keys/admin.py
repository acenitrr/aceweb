from django.contrib import admin
from .models import *

class keys_dataAdmin(admin.ModelAdmin):
	list_display=["username","password","port","host","flag"]

admin.site.register(keys_data,keys_dataAdmin)
# Register your models here.

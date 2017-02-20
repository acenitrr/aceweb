from django.contrib import admin
from .models import *

class internal_key_dataAdmin(admin.ModelAdmin):
	list_display=["key","value"]

admin.site.register(internal_key_data,internal_key_dataAdmin)

# Register your models here.

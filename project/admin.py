from django.contrib import admin
from .models import *

class project_dataAdmin(admin.ModelAdmin):
	list_display=["title","issuer","date_issued",'active','file']

admin.site.register(project_data,project_dataAdmin)

# Register your models here.

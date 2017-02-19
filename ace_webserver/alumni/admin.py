from django.contrib import admin
from .models import *

class alumni_dataAdmin(admin.ModelAdmin):
	list_display=["enroll_no","name","mobile","email","current_status","company_institue","designation","other"]

admin.site.register(alumni_data,alumni_dataAdmin)

# Register your models here.

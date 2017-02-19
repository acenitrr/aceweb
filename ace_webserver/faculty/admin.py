from django.contrib import admin
from .models import *

class faculty_dataAdmin(admin.ModelAdmin):
	list_display=["faculty_id","name","designation","education","email","mobile","photo"]

admin.site.register(faculty_data,faculty_dataAdmin)

class area_of_interest_dataAdmin(admin.ModelAdmin):
	list_display=["faculty_id","area_of_interest"]

admin.site.register(area_of_interest_data,area_of_interest_dataAdmin)

class other_detailsAdmin(admin.ModelAdmin):
	list_display=["faculty_id","other_details"]

admin.site.register(other_details_data,other_detailsAdmin)

# Register your models here.

from django.contrib import admin
from .models import *

class alumni_dataAdmin(admin.ModelAdmin):
	list_display=["roll_no","name","mobile","email","current_status","company_institue","designation","other","photo",'batch']

admin.site.register(alumni_data,alumni_dataAdmin)

# Register your models here.

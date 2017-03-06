from django.contrib import admin
from .models import *
# Register your models here.
class overall_achievement_dataAdmin(admin.ModelAdmin):
	list_display=["title","description","photo"]

admin.site.register(overall_achievement_data,overall_achievement_dataAdmin)


class training_placement_achievement_dataAdmin(admin.ModelAdmin):
	list_display=["title","description","photo"]

admin.site.register(training_placement_achievement_data,training_placement_achievement_dataAdmin)


class academics_achievement_dataAdmin(admin.ModelAdmin):
	list_display=["title","description","photo"]
admin.site.register(academics_achievement_data,academics_achievement_dataAdmin)


class cocurricular_achievement_dataAdmin(admin.ModelAdmin):
	list_display=["title","description","photo"]
admin.site.register(cocurricular_achievement_data,cocurricular_achievement_dataAdmin)


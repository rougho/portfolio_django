from django.contrib import admin
from near_me.admin import Shops
from django.contrib.gis.admin import OSMGeoAdmin
from projects.models import (Project,
                            AboutEducation,
                            AboutExperience,
                            AboutSkills, 
                            AboutLanguages,
                            AboutInterests)

# Register your models here.

@admin.register(Shops)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name' , 'location')

admin.site.register(Project)
admin.site.register(AboutEducation)
admin.site.register(AboutExperience)
admin.site.register(AboutSkills)
admin.site.register(AboutLanguages)
admin.site.register(AboutInterests)
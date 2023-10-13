from django.contrib import admin
from projects.models import (Project,
                            AboutEducation,
                            AboutExperience,
                            AboutSkills, 
                            AboutLanguages,
                            AboutInterests)

# Register your models here.
admin.site.register(Project)
admin.site.register(AboutEducation)
admin.site.register(AboutExperience)
admin.site.register(AboutSkills)
admin.site.register(AboutLanguages)
admin.site.register(AboutInterests)
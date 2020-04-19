from django.contrib import admin
from resume.models import Experience, Course, Extracurricular, Skill

class ExperienceAdmin(admin.ModelAdmin):
    pass

class CourseAdmin(admin.ModelAdmin):
     pass

class ExtracurricularAdmin(admin.ModelAdmin):
     pass

class SkillAdmin(admin.ModelAdmin):
    pass

admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Extracurricular, ExtracurricularAdmin)
admin.site.register(Skill, SkillAdmin)
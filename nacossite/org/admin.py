from django.contrib import admin
from .models import Session,Course,Level,Material


class SessionAdmin(admin.ModelAdmin):
    list_display=('session',)

class CourseAdmin(admin.ModelAdmin):
    list_display=('title','code',)

class LevelAdmin(admin.ModelAdmin):
    list_display=('level',)

class MaterialAdmin(admin.ModelAdmin):
    list_display=('title',)


admin.site.register(Session, SessionAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Material, MaterialAdmin)


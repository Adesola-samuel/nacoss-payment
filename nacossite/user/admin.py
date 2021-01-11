from django.contrib import admin
from .models import Biodata


class BiodataAdmin(admin.ModelAdmin):
    list_display=('matric_number','user','level','session_admitted')


admin.site.register(Biodata, BiodataAdmin)
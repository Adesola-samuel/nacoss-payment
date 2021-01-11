from django.contrib import admin
from .models import Transaction, Due


class TransactionAdmin(admin.ModelAdmin):
    list_display=('user','due','date')

class DueAdmin(admin.ModelAdmin):
    list_display=('title','amount','description')


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Due, DueAdmin)
from django.contrib import admin
from . models import Work

# Register your models here.

class WorkAdmin(admin.ModelAdmin):
    list_display = ['id','place','created','updated','Name','about_work','choose','amount']
    search_fields = ('name','place','about_work')
    search_filter = ('name','place','created','updated','amount')

admin.site.register(Work,WorkAdmin)    
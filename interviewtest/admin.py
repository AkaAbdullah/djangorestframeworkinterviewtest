from django.contrib import admin
from .models import Interview
# Register your models here.

@admin.register(Interview)

class InterviewAdmin(admin.ModelAdmin):
    list_display = ('id','name','date', 'description')
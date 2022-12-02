from django.contrib import admin
from .models import *

admin.site.site_header = "My Resume"

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'description', 'created_at')
    search_fields = ('name', 'email', 'phone_number', 'description')
    list_per_page = 6

# Register your models here.
admin.site.register(Message, MessageAdmin)
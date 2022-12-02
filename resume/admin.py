from django.contrib import admin
from .models import *

admin.site.site_header = "My Resume"

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')

# Register your models here.
admin.site.register(Message)
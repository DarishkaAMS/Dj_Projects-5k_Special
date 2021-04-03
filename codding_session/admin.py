from django.contrib import admin
from django.contrib.admin import ModelAdmin
from codding_session.models import CoddingSession


# Register your models here.

@admin.register(CoddingSession)
class CoddingSessionAdmin(ModelAdmin):
    list_display = ['id', 'name', 'language', 'link', 'starting_time']

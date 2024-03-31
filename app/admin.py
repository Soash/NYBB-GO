from django.contrib import admin
from .models import Team, Start

class Team_display(admin.ModelAdmin):
    list_display = ('name','score',)

class Start_display(admin.ModelAdmin):
    list_display = ('name','start',)

admin.site.register(Team, Team_display)
admin.site.register(Start, Start_display)
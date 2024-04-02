from django.contrib import admin
from .models import Team, Start, CompetitionSettings

class Team_display(admin.ModelAdmin):
    list_display = ('name','score',)

class Start_display(admin.ModelAdmin):
    list_display = ('name','start',)

class CompetitionSettingsAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'over_time')

admin.site.register(Team, Team_display)
admin.site.register(Start, Start_display)
admin.site.register(CompetitionSettings, CompetitionSettingsAdmin)



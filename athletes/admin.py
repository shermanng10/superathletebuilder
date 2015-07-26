from django.contrib import admin

from .models import Athlete, League, Team, Sport

class AthleteInline(admin.TabularInline):
	model = Athlete
	extra = 1

class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'created_at', 'updated_at')
	inlines = [AthleteInline]

class SportAdmin(admin.ModelAdmin):
	list_display = ('name', 'created_at', 'updated_at')

class LeagueAdmin(admin.ModelAdmin):
	list_display = ('name', 'created_at', 'updated_at')

class AthleteAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'sport', 'league', 'team', 'created_at', 'updated_at')

admin.site.register(Athlete, AthleteAdmin)
admin.site.register(League, LeagueAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Sport, SportAdmin)

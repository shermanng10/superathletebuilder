from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
  url(r'^admin/', include(admin.site.urls)),
  url(r'^athletes/', include('athletes.athlete_urls')),
  url(r'^sports/', include('athletes.sport_urls')),
  url(r'^leagues/', include('athletes.league_urls')),
  url(r'^teams/', include('athletes.team_urls')),
]

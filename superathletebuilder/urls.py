from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
 	url(r'^$', include('athletes.app_urls.home_urls')),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^leagues/', include('athletes.app_urls.league_urls')),
  url(r'^athletes/', include('athletes.app_urls.athlete_urls')),
  url(r'^sports/', include('athletes.app_urls.sport_urls')),
  url(r'^teams/', include('athletes.app_urls.team_urls')),
]

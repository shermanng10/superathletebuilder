from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.league_index, name='index'),
	url(r'^(?P<league_id>[0-9]+)/$', views.league_detail, name='detail'),
	url(r'^new/$', views.new_league, name='new_league'),
]


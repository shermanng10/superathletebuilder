from django.conf.urls import url

from .. import views

urlpatterns = [
	url(r'^$', views.LeagueIndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.LeagueDetailView.as_view(), name='detail'),
	url(r'^new/$', views.new_league, name='new_league'),
]


from django.conf.urls import url

from .. import views

urlpatterns = [
	url(r'^$', views.LeagueIndexView.as_view(), name='league_index'),
	url(r'^new/$', views.NewLeagueView.as_view(), name='new_league'),
	url(r'^(?P<pk>[0-9]+)/$', views.LeagueDetailView.as_view(), name='league_detail'),
]


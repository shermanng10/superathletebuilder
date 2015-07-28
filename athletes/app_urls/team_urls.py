from django.conf.urls import url

from .. import views

urlpatterns = [
	url(r'^$', views.TeamIndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.TeamDetailView.as_view(), name='detail'),
	url(r'^new/$', views.NewTeamView.as_view(), name='new_team'),
]


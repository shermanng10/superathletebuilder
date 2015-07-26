from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.team_index, name='index'),
	url(r'^(?P<team_id>[0-9]+)/$', views.team_detail, name='detail'),
	url(r'^new/$', views.new_team, name='new_team'),
]


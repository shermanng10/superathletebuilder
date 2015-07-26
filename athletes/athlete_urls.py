from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.athlete_index, name='index'),
	url(r'^(?P<athlete_id>[0-9]+)/$', views.athlete_detail, name='detail'),
	url(r'^new/$', views.new_athlete, name='new_athlete'),
]


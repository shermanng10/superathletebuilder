from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.sport_index, name='index'),
	url(r'^(?P<sport_id>[0-9]+)/$', views.sport_detail, name='detail'),
	url(r'^new/$', views.new_sport, name='new_sport'),
]


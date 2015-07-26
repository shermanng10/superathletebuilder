from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.AthleteIndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.AthleteDetailView.as_view(), name='detail'),
	url(r'^new/$', views.new_athlete, name='new_athlete'),
]


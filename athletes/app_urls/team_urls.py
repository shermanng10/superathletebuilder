from django.conf.urls import url

from .. import views

urlpatterns = [
	url(r'^$', views.TeamIndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.TeamDetailView.as_view(), name='detail'),
	url(r'^new/$', views.new_team, name='new_team'),
]


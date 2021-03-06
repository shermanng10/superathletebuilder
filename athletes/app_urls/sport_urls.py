from django.conf.urls import url

from .. import views

urlpatterns = [
	url(r'^$', views.SportIndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.SportDetailView.as_view(), name='detail'),
	url(r'^new/$', views.NewSportView.as_view(), name='new_sport'),
]


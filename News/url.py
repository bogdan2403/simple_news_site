from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^news/(?P<id>[0-9]+)$', views.news, name='news'),
    url(r'^ajax/$', views.ajax, name='ajax'),
]
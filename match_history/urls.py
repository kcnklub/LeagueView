from django.conf.urls import url
from . import views

app_name = 'match_history'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search_summoner/$', views.search_summoner, name='search_summoner'),
    url(r'^(?P<game_id>[0-9]+)/$', views.detail, name='detail')
]
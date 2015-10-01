from django.conf.urls import patterns, url
from eventpage import views

urlpatterns = patterns('',
        url(r'^event=(?P<event_id>\d+)/$', views.get_event_page_json, name='index'),
)    

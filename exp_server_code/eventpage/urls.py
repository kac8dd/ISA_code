from django.conf.urls import patterns, url
from eventpage import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
)    

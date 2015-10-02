"""exp_server_code URL Configuration
	The urls here redirect queries to the appropriate service app
"""
from django.conf.urls import include, url
from django.contrib import admin
from exp_server_code import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/home/', include('homepage.urls')),
    url(r'^api/v1/view_event/', include('eventpage.urls')), 
]

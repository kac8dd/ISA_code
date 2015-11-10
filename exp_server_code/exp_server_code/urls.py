"""exp_server_code URL Configuration
	The urls here redirect queries to the appropriate service app
"""
from django.conf.urls import include, url
from django.contrib import admin
from exp_server_code import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/user/create/$', views.create_user, name='CreateUser'),
    url(r'^api/v1/user/logout/$', views.logout, name='Logout'),
    url(r'^api/v1/user/login/$', views.login, name='Login'),
    url(r'^api/v1/home/', include('homepage.urls')),
    url(r'^api/v1/view_event/', include('eventpage.urls')), 
    url(r'^api/v1/event/create/$', views.create_event, name='CreateEvent'),
    url(r'^api/v1/event/search/$', views.search_event, name='SearchEvent'),


]

"""exp_server_code URL Configuration
	The urls here redirect queries to the appropriate service app
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', include('homepage.urls')),
    url(r'^view_event/', include('eventpage.urls')), 
]

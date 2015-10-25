from django.conf.urls import include, url
from django.contrib import admin
from web_frontend_server_code import views

urlpatterns = [
    url(r'^$', views.index, name='Events'),
    url(r'^events/(?P<event_id>\d+)/$', views.details, name='Details'),
    url(r'^events/create/$', views.add_event, name='AddEvent'),
    url(r'^user/create/$', views.create_user, name='CreateUser'),
    url(r'^login/$', views.login, name='Login'),
    url(r'^logout/$', views.logout, name='Logout'),
    url(r'^admin/', include(admin.site.urls)),
]

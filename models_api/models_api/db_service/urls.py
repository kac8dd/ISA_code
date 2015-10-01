from django.conf.urls import patterns, url

from ticket import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^api/v1/create/event/$', views.create_event, name='createEvent'),
	url(r'^api/v1/create/ticket/$',views.create_ticket, name='createTicket'),
	url(r'^api/v1/create/user/$',views.create_user, name='createUser'),
	
	url(r'^api/v1/update/event/(?P<event_id>\d+)/$',views.update_event,name='updateEvent'),
	url(r'^api/v1/update/ticket/(?P<ticket_id>\d+)/$',views.update_ticket,name='updateTicket'),
	url(r'^api/v1/update/user/(?P<event_id>\d+)/',views.update_user,name='updateUser'),
	
	url(r'^api/v1/event/(?P<event_id>\d+)/$$',views.event,name='event'),
	url(r'^api/v1/ticket/(?P<ticket_id>\d+)/$',views.ticket,name='ticket'),
	url(r'^api/v1/user/(?P<userp_id>\d+)/$',views.user,name='user'),
	
	
)
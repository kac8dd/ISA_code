from django.conf.urls import patterns, url

from db_service import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^api/v1/create/event/$', views.create_event, name='createEvent'),
	url(r'^api/v1/create/ticket/$',views.create_ticket, name='createTicket'),
	url(r'^api/v1/create/user/$',views.create_user, name='createUser'),
	url(r'^api/v1/create/purchase/$',views.create_purchase, name='createPurchase'),
	url(r'^api/v1/create/authenticator/$',views.create_authenticator, name='createAuthenticator'),
	
	url(r'^api/v1/update/event/(?P<event_id>\d+)/$',views.update_event,name='updateEvent'),
	url(r'^api/v1/update/ticket/(?P<ticket_id>\d+)/$',views.update_ticket,name='updateTicket'),
	url(r'^api/v1/update/user/(?P<user_id>\d+)/',views.update_user,name='updateUser'),
	#url(r'^api/v1/update/purchase/(?P<purchase_id>\d+)/',views.update_purchase,name='updatePurchase'),
	url(r'^api/v1/user/logout/',views.logout,name='Logout'),
	
	url(r'^api/v1/get/event/(?P<event_id>\d+)/$',views.get_event,name='event'),
	url(r'^api/v1/get/ticket/(?P<ticket_id>\d+)/$',views.get_ticket,name='ticket'),
	url(r'^api/v1/get/user/(?P<user_id>\d+)/$',views.get_user,name='user'),
	url(r'^api/v1/get/purchase/(?P<purchase_id>\d+)/$',views.get_purchase,name='purchase'), 
	url(r'^api/v1/get/latest/(?P<count>[1-50])/$', views.get_latest,name='latest'),	
	url(r'^api/v1/user/authenticate/$',views.authenticate,name='Authenticate'), 
	url(r'^api/v1/user/validate/$',views.validate,name='Validate'), 


)

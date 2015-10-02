from django.conf.urls import url

from . import views

# host/events/...
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/', views.addevent, name='addevent'),
    url(r'^(?P<event_id>.*)/', views.details, name='details'),

]
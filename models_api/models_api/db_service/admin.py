from django.contrib import admin
from ticket.models import UserProfile, Event, Purchase, Ticket
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Event)
admin.site.register(Purchase)
admin.site.register(Ticket)

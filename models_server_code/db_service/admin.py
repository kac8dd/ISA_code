from django.contrib import admin
from db_service.models import User, Event, Purchase, Ticket
# Register your models here.

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Purchase)
admin.site.register(Ticket)

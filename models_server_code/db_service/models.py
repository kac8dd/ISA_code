from django.db import models
#from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=24, unique=True)
	date_joined = models.DateTimeField()
	firstname = models.CharField(max_length=16)
	lastname = models.CharField(max_length=16)
	password = models.CharField(max_length=96)
	is_active = models.BooleanField(default=False)

	def full_name(self):
		return self.firstname+" "+self.lastname

	def __str__(self):
		return self.full_name()

class Event(models.Model):
	name = models.CharField(max_length=300)
	description = models.CharField(max_length=5000)
	start_time = models.DateTimeField(default=datetime.datetime.now)
	pub_date = models.DateTimeField(default=datetime.datetime.now)
	location = models.CharField(max_length=1000)
	creator = models.ForeignKey(User)
	#ticket = models.OneToOneField(Ticket, default=none)

	def __str__(self):
		return self.name

class Ticket(models.Model):
	
	price = models.FloatField()
	event = models.ForeignKey(Event)
	amount = models.IntegerField()
	
	def __str__(self):
		return self.event.name+" - "+str(self.id)

class Purchase(models.Model):
	buyer = models.OneToOneField(User)
	ticket = models.OneToOneField(Ticket)
	date = models.DateTimeField(default=datetime.datetime.now)

	def __str__(self):
		full_name = self.user_profile.full_name()
		return full_name + " purchases " + self.ticket.name

class Authenticator(models.Model):
	authenticator = models.CharField(max_length=100, primary_key=True)
	user_id = models.IntegerField()
	date_created = models.DateTimeField(default=datetime.datetime.now)

	def __str__(self):
		return "authenticator for user_id=="+str(self.user_id)
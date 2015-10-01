from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	
	def full_name(self):
		return self.first_name+" "+self.last_name

	def __str__(self):
		return self.full_name()

class Event(models.Model):
	name = models.CharField(max_length=300)
	description = models.CharField(max_length=5000)
	start_time = models.DateTimeField(default=datetime.datetime.today)
	pub_date = models.DateTimeField(default=datetime.datetime.today)
	location = models.CharField(max_length=1000)

	def __str__(self):
		return self.name

class Ticket(models.Model):
	name = models.CharField(max_length=300)
	price = models.FloatField()
	event = models.ForeignKey(Event)
	amount = models.IntegerField()

	def __str__(self):
		return self.event.name+" - "+self.name

class Purchase(models.Model):
	user_profile = models.OneToOneField(UserProfile)
	ticket = models.OneToOneField(Ticket)
	date = models.DateTimeField(default=datetime.datetime.today)

	def __str__(self):
		full_name = self.user_profile.full_name()
		return full_name + " purchases " + self.ticket.name
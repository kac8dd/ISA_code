from django.shortcuts import render
from ticket.models import UserProfile, Event, Ticket, Purchase

# response
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.core.urlresolvers import reverse

# authenticate
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import hashers
# Create your views here.
def index(request):
	return HttpResponse('Hello!')

def create_event(request):
	if request.method != 'POST':
		return HttpResponse('must make POST request')
	name = request.POST['name']
	description = request.POST['description']
	start_time = request.POST['start_time']
	location = request.POST['location']
	event = Event(name=name,description=description,start_time=start_time,location=location)
	try:
		event.save()
	except db.Error:
		return _error_response(request,'db error')

	return _success_response(request,{'event':event.id})

def update_event(request,event_id):
	if request.method != 'POST':
		return HttpResponse('must make POST request')
	try:
		event = Event.objects.get(pk=event_id)
	except models.Event.DoesNotExist:
		return _error_response(request,'event not found')

	changed = False
	if 'name' in request.POST:
		event.name=request.POST['name']
		changed=True
	if 'description' in request.POST:
		event.description=request.POST['description']
		changed=True
	if 'start_time' in request.POST:
		event.start_time=request.POST['start_time']
		changed=True
	if 'location' in request.POST:
		event.location=request.POST['location']
		changed=True

	if not changed:
		return _error_response(request,'no field updated')
	event.save()
	return _success_response(request,'success')

def event(request,event_id):
	if request.method != 'GET':
		return HttpResponse('must make GET request')
	try:
		event = Event.objects.get(pk=event_id)
	except:
		return _error_response(request,'event not found')

	return _success_response(request,{'event_id':event.id,'name':event.name,'description':event.description,'start_time':event.start_time,'pub_date':event.pub_date,'location':event.location})

def create_ticket(request):
	if request.method != 'POST':
		return _error_response('must make POST request')
	name = request.POST['name']
	price = request.POST['price']
	event_id = request.POST['event_id']
	amount = request.POST['amount']
	event = Event.objects.get(pk=event_id)
	ticket = Ticket(name=name,price=price,event=event,amount=amount)
	try:
		ticket.save()
	except db.Error:
		return _error_response(request,'db error')
	return _success_response(request,{'ticket_id':ticket.id})

def update_ticket(request,ticket_id):
	if request.method != 'POST':
		return _error_response(request,'must make POST request')
	try:
		ticket = Ticket.objects.get(pk=ticket_id)
	except models.Ticket.DoesNotExist:
		return _error_response(request,'ticket not found')

	changed = False
	if 'name' in request.POST:
		ticket.name = request.POST['name']
		changed = True
	if 'price' in request.POST:
		ticket.price = request.POST['price']
		changed = True
	if 'amount' in request.POST:
		ticket.amount = request.POST['amount']
		changed = True

	if not changed:
		return _error_response(request,'no field updated')
	ticket.save()

	return _success_response(request,'success')

def ticket(request,ticket_id):
	if request.method != 'GET':
		return _error_response(request,'must make GET request')
	try:
		ticket = Ticket.objects.get(pk=ticket_id)
	except:
		return _error_response(request,'ticket not found')

	return _success_response(request,{'ticket_id':ticket.id,'name':ticket.name,'price':ticket.price,'event':ticket.event.name,'amount':ticket.amount})


def create_user(request):
	if request.method != 'POST':
		return _error_response(request,'must make POST request')
	username = request.POST['username']
	password = hasher.make_passworkd(request.POST['password'])
	firstname = request.POST['firstname']
	lastname = request.POST['lastname']
	user = User(username=username,password=password)
	try:
		user.save()
	except:
		return _error_response(request,'db error')
	user_profile = UserProfile(firstname=firstname,lastname=lastname,user=user)
	try:
		user_profile.save()
	except:
		return _error_response(request,'db error')
	return _success_response(request,'success')

def update_user(request,userp_id):
	if request.method != 'POST':
		return _error_response(request,'must make POST request')
	try:
		user_p = UserProfile.objects.get(pk=userp_id)
	except models.UserProfile.DoesNotExist:
		return _error_response(request,'User not found')
	changed = False
	user = user_p.user

	if 'firstname' in request.POST:
		user_p.firstname=request.POST['firstname']
		changed=True
	if 'lastname' in request.POST:
		user_p.lastname=request.POST['lastname']
		changed=True
	if 'password' in request.POST:
		user.password = hasher.make_password(request.POST['password'])
		changed=True

	if not changed:
		return _error_response(request,'no field updated')
	user_p.save()
	user.save()
	return _success_response(request,'success')

def user(request,userp_id):
	if request.method != 'GET':
		return _error_response(request,'must make GET request')
	try:
		user_p = UserProfile.objects.get(pk=userp_id)
		user = user_p.user
	except:
		return _error_response(request,'user not found')

	return _success_response(request,{'user_id':user_p.id,'username':user.username,'first_name':user_p.first_name,'last_name':user_p.last_name})

def _error_response(request,error_msg):
	return JsonResponse({'ok': False, 'error': error_msg})

def _success_response(request,resp=None):
	if resp:
		return JsonResponse({'ok': True, 'resp': resp})
	else:
		return JsonResponse({'ok': True})

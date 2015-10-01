from django.shortcuts import render
from db_service.models import UserProfile, Event, Ticket, Purchase

# response
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict

# authenticate
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import hashers 

#these are not front faceing POSTs so we don't need csrf tokens
from django.views.decorators.csrf import csrf_exempt

#database transactions
from django.db import IntegrityError, transaction

import json

# Create your views here.
def index(request):
	return HttpResponse('Hello!')

@csrf_exempt
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
	except IntegrityError:
		return _error_response(request,'db error, unable to save event')

	return _success_response(request,{'Event successfully created->event_id':event.id})

@csrf_exempt
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
	return _success_response(request,'Event successfully updated')

@csrf_exempt
def get_event(request,event_id):
	if request.method != 'GET':
		return HttpResponse('must make GET request')
	try:
		event = Event.objects.get(pk=event_id)
	except:
		return _error_response(request,'event not found')

	return _success_response(request,{'event_id':event.id,'name':event.name,'description':event.description,'start_time':event.start_time,'pub_date':event.pub_date,'location':event.location})

@csrf_exempt
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
	return _success_response(request,{'ticket successfully created->ticket_id':ticket.id})

@csrf_exempt
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

	return _success_response(request,'Event successfully updated')

@csrf_exempt
def get_ticket(request,ticket_id):
	if request.method != 'GET':
		return _error_response(request,'must make GET request')
	try:
		ticket = Ticket.objects.get(pk=ticket_id)
	except:
		return _error_response(request,'ticket not found')

	return _success_response(request,{'ticket_id':ticket.id,'name':ticket.name,'price':ticket.price,'event':ticket.event.name,'amount':ticket.amount})

@csrf_exempt
def create_user(request):
	if request.method != 'POST':
		return _error_response(request,'must make POST request')
	username_input = request.POST['username']
	password_input = hashers.make_password(request.POST['password'])
	firstname_input = request.POST['firstname']
	lastname_input = request.POST['lastname']
	user = User(username=username_input,password=password_input)
	try:
		user.save()
	except:
		return _error_response(request,'db error')
	user_profile = UserProfile(first_name=firstname_input,last_name=lastname_input,user=user)
	try:
		user_profile.save()
	except:
		return _error_response(request,'db error')
	return _success_response(request,{'user successfully created->user_id':user_profile.id})

@csrf_exempt
def update_user(request,user_id):
	if request.method != 'POST':
		return _error_response(request,'must make POST request')
	try:
		user_p = UserProfile.objects.get(pk=user_id)
	except models.UserProfile.DoesNotExist:
		return _error_response(request,'User not found')
	changed = False
	user = user_p.user

	if 'firstname' in request.POST:
		user_p.first_name=request.POST['firstname']
		changed=True
	if 'lastname' in request.POST:
		user_p.last_name=request.POST['lastname']
		changed=True
	if 'password' in request.POST:
		user.password = hashers.make_password(request.POST['password'])
		changed=True

	if not changed:
		return _error_response(request,'no field updated')
	
	user_p.save()
	user.save()
	return _success_response(request,'user successfully updated')

def get_user(request,user_id):
	if request.method != 'GET':
		return _error_response(request,'must make GET request')
	try:
		user_p = UserProfile.objects.get(pk=user_id)
		user = user_p.user
	except:
		return _error_response(request,'user not found')

	return _success_response(request,{'user_id':user_p.id,'username':user.username,'first_name':user_p.first_name,'last_name':user_p.last_name})

@csrf_exempt
def create_purchase(request):
        if request.method != 'POST':
                return _error_response('must make POST request')
        user_profile_input = UserProfile.objects.get(pk=request.POST['user_id']) 
        ticket_input = Ticket.objects.get(pk=request.POST['ticket_id']) 
        purchase = Purchase(user_profile=user_profile_input,ticket=ticket_input,)
        try:
                purchase.save()
        except db.Error:
                return _error_response(request,'db error')
        return _success_response(request,{'purchase successfully created->purchase_id':purchase.id})

def get_purchase(request, purchase_id):
        if request.method != 'GET':
                return _error_response(request,'must make GET request')
        try:
                purchase = Purchase.objects.get(pk=purchase_id)
        except:
                return _error_response(request,'purchase not found')

        return _success_response(request,{'purchase_id':purchase_id,'user_id':purchase.user_profile.id, 'ticket_id':purchase.ticket.id,'date':purchase.date})

def get_latest(request, count):
	response = ""
	x = 0
	current_event_id = Event.objects.latest('pub_date').id 
	while x < int(count):
		event = Event.objects.get(pk=current_event_id)
		event.pub_date = str(event.pub_date) 
		event.start_time = str(event.start_time)
		response += json.dumps(model_to_dict(event))+"-" 
		current_event_id -= 1
		x += 1 
	return _success_response(request, response)	
 
def _error_response(request,error_msg):
	return JsonResponse({'ok': False, 'error': error_msg})

def _success_response(request,resp=None):
	if resp:
		return JsonResponse({'ok': True, 'resp': resp})
	else:
		return JsonResponse({'ok': True})

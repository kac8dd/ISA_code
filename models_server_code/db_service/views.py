import datetime
import os
import base64

from django.shortcuts import render
from db_service.models import User, Event, Ticket, Purchase, Authenticator
from db_service import models
# response
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict

# authenticate
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import hashers 

#these are not front faceing POSTs so we don't need csrf tokens
from django.views.decorators.csrf import csrf_exempt

#database transactions
from django.db import IntegrityError, transaction
from django import db

import json

# Create your views here.
def index(request):
    return HttpResponse('This is the models api.')

def create_event(request):
    if request.method != 'POST':
        return HttpResponse('must make POST request')
    if not 'name' in request.POST or \
        not 'description' in request.POST or \
        not 'location' in request.POST or \
        not 'start_time' in request.POST or \
        not 'creator_id' in request.POST:
        return _error_response(request,"missing required fields")
    name = request.POST['name']
    description = request.POST['description']
    start_time = request.POST['start_time']
    location = request.POST['location']
    creator_id = request.POST['creator_id']
    
    creator = User.objects.get(pk=creator_id)
    event = Event(name=name, \
        description=description, \
        start_time=start_time, \
        location=location, \
        creator=creator)
    try:
        event.save()
    except IntegrityError:
        return _error_response(request,'db error, unable to save event')

    print("new event, id = "+str(event.id))
    return _success_response(request,{'event_id':event.id})

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

def get_event(request,event_id):
    if request.method != 'GET':
        return HttpResponse('must make GET request')
    try:
        event = Event.objects.get(pk=event_id)
    except:
        return _error_response(request,'event not found')

    event.start_time = str(event.start_time)
    event.pub_date = str(event.pub_date)
    return JsonResponse(model_to_dict(event))

def create_ticket(request):
    if request.method != 'POST':
        return _error_response('must make POST request')
    if 'price' not in request.POST or \
        'event_id' not in request.POST or \
        'amount' not in request.POST:
        return _error_response(request, "missing required fields")
    price = request.POST['price']
    event_id = request.POST['event_id']
    amount = request.POST['amount']
    event = Event.objects.get(pk=event_id)
    ticket = Ticket(price=price,event=event,amount=amount)
    try:
        ticket.save()
    except db.Error:
        return _error_response(request,'db error, unable to save ticket')
    return _success_response(request,{'ticket successfully created->ticket_id':ticket.id})

def update_ticket(request,ticket_id):
    if request.method != 'POST':
        return _error_response(request,'must make POST request')
    try:
        ticket = Ticket.objects.get(pk=ticket_id)
    except models.Ticket.DoesNotExist:
        return _error_response(request,'ticket not found')

    changed = False
    if 'price' in request.POST:
        ticket.price = request.POST['price']
        changed = True
    if 'amount' in request.POST:
        ticket.amount = request.POST['amount']
        changed = True

    if not changed:
        return _error_response(request,'no field updated')
    ticket.save()

    return _success_response(request,'Ticket successfully updated')

def get_ticket(request,ticket_id):
    if request.method != 'GET':
        return _error_response(request,'must make GET request')
    try:
        ticket = Ticket.objects.get(pk=ticket_id)
    except:
        return _error_response(request,'ticket not found')

    return JsonResponse(model_to_dict(ticket))

def create_user(request):
    if request.method != 'POST':
        return _error_response(request,'must make POST request')
    if 'firstname' not in request.POST or \
        'lastname' not in request.POST or \
        'password' not in request.POST or \
        'username' not in request.POST:
        return _error_response(request, "missing required fields")
    username = request.POST['username']
    password = hashers.make_password(request.POST['password'])
    firstname_input = request.POST['firstname']
    lastname_input = request.POST['lastname']
    user = User(username=username, \
        firstname=firstname_input, \
        lastname=lastname_input, \
        password=password, \
        date_joined=datetime.datetime.now()
        )
    try:
        user.save()
    except db.Error:
        return _error_response(request, "db error: username conflicts")
    
    return _success_response(request,{'user_id':user.pk})

def update_user(request,user_id):
    if request.method != 'POST':
        return _error_response(request,'must make POST request')
    try:
        user = User.objects.get(pk=user_id)
    except models.User.DoesNotExist:
        return _error_response(request,'User not found')
    changed = False
    
    if 'firstname' in request.POST:
        user.firstname=request.POST['firstname']
        changed=True
    if 'lastname' in request.POST:
        user.lastname=request.POST['lastname']
        changed=True
    if 'password' in request.POST:
        user.password = hashers.make_password(request.POST['password'])
        changed=True

    if not changed:
        return _error_response(request,'no field updated')
    
    user.save()
    return _success_response(request,'user successfully updated')

def get_user(request,user_id):
    if request.method != 'GET':
        return _error_response(request,'must make GET request')
    try:
        user = User.objects.get(pk=user_id)
    except:
        return _error_response(request,'user not found')

    return JsonResponse(model_to_dict(user))

def create_purchase(request):
        if request.method != 'POST':
            return _error_response('must make POST request')
        if 'user_id' not in request.POST or \
            'ticket_id' not in request.POST:
            return _error_response(request, "missing required fields")
        user_input = User.objects.get(pk=request.POST['user_id']) 
        ticket_input = Ticket.objects.get(pk=request.POST['ticket_id']) 
        purchase = Purchase(buyer=user_input,ticket=ticket_input,)
        try:
            purchase.save()
        except db.Error:
            return _error_response(request,'db error, unable to save purchase')
        return _success_response(request,{'purchase successfully created->purchase_id':purchase.id})

def get_purchase(request, purchase_id):
        if request.method != 'GET':
            return _error_response(request,'must make GET request')
        try:
            purchase = Purchase.objects.get(pk=purchase_id)
        except:
            return _error_response(request,'purchase not found')
        purchase.date = str(purchase.date) 
        return JsonResponse(model_to_dict(purchase))

def create_authenticator(request):
    if request.method != 'POST':
        return _error_response(request,'must make POST request')
    if 'user_id' not in request.POST:
        return _error_response(request,"missing required fields")
    user_id = request.POST['user_id']
    try:
        user = User.objects.get(pk=user_id)
    except models.User.DoesNotExist:
        return _error_response(request, 'user does not exist')
    auth = Authenticator.objects.filter(user_id = user_id)
    if auth:
        auth = auth.first()
        return _success_response(request,{'authenticator':auth.authenticator})
    authenticator = base64.b64encode(os.urandom(32)).decode('utf-8')
    auth = Authenticator(authenticator=authenticator,user_id=user_id)
    try:
        auth.save()
    except db.Error:
        return _error_response(request, "db error")
    return _success_response(request,{'authenticator':auth.authenticator})

def validate(request):
    """
    authenticate using username and password
    """
    if request.method != "POST":
        return _error_response(request, "must make POST request")
    if "username" not in request.POST or \
        "password" not in request.POST:
        return _error_response(request, "missing required fields")
    username = request.POST["username"]
    password = request.POST["password"]
    try:
        user = User.objects.get(username = username)
    except models.User.DoesNotExist:
        return _error_response(request, "User not found")
    is_correct = hashers.check_password(password, user.password)
    if is_correct:
        return _success_response(request, {"user_id":user.pk})
    else:
        return _error_response(request, "Username and password do not match.")


def authenticate(request):
    """
    authenticate using authenticator
    """
    if request.method != 'POST':
        return _error_response(request, 'must make POST request')
    if 'authenticator' not in request.POST:
        return _error_response(request, "missing required fields")
    authenticator = request.POST['authenticator']
    try:
        auth = Authenticator.objects.get(pk=authenticator)
    except:
        return _error_response(request, 'authenticator not found')
    return _success_response(request, {'user_id':auth.user_id})

def logout(request):
    if request.method != 'POST':
        return _error_response(request, 'must make POST request')
    if 'authenticator' not in request.POST:
        return _error_response(request, "missing required fields")
    authenticator = request.POST['authenticator']
    try:
        auth = Authenticator.objects.get(pk=authenticator)
        user_id = auth.user_id
        auth.delete()
        return _success_response(request, {'userid':user_id})
    except:
        return _error_response(request,"Authenticator not found or cannot delete")
    

def get_latest(request, count):
    count = min(int(count), len(Event.objects.all()))
    response = {}
    events = Event.objects.all().order_by('-pub_date') 
    
    for i in range(count):
        event = events[i]
        response[event.id] = model_to_dict(event)
    #print(str(response))
    return JsonResponse(response)    
 
def _error_response(request,error_msg):
    return JsonResponse({'ok': False, 'error': error_msg})

def _success_response(request,resp=None):
    if resp:
        return JsonResponse({'ok': True, 'resp': resp})
    else:
        return JsonResponse({'ok': True})

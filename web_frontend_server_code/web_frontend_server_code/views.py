from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render
from web_frontend_server_code.forms import LoginForm, EventForm, UserForm
import urllib
from urllib.parse import urlencode
import json
from urllib.error import HTTPError
from django.core.urlresolvers import reverse

def index(request):
	# auth = request.COOKIES.get("auth")
	# if auth:
	# 	firstname = request.COOKIES.get("firstname")
	# 	lastname = request.COOKIES.get("lastname")
	# else:
	# 	firstname = lastname = None

	try:
		with urllib.request.urlopen("http://exp_host:8000/api/v1/home/") as url:
			latest_events_json = url.read()
		resp = json.loads(latest_events_json.decode('utf-8'))
		events = []
		for key, value in resp.items():
			events.append(value)
	except HTTPError:
		events = "read from exp_host failed"
	return render(request, 'eventlist.html', {
		'events': events,
	})

def details(request, event_id):
	url = "http://exp_host:8000/api/v1/view_event/" + event_id + "/"
	try:
		with urllib.request.urlopen(url) as url:
			details_json = url.read()
		jsondict = json.loads(details_json.decode('utf-8'))
	except HTTPError:
		return render(request, 'eventdetails.html', {
			'error': True,
			'errormsg': "something went wrong. the event you're looking for probably doesn't exist",
		})
	return render(request, 'eventdetails.html', {
		'error': False,
		'creator_id': jsondict['creator'],
		'event_id': jsondict['id'],
		'pub_date': jsondict['pub_date'],
		'event_name': jsondict['name'],
		'event_desc': jsondict['description'],
		'event_location': jsondict['location'],
		'event_start_time': jsondict['start_time'],
		'jsonstring': jsondict,
	})

def create_user(request):
	if request.method == 'POST':
		if 'username' not in request.POST or \
			'password' not in request.POST or \
			'firstname' not in request.POST or \
			'lastname' not in request.POST:
			return HttpResponse('missing required fields')
		post_value = {
			'username':request.POST['username'],
			'firstname':request.POST['firstname'],
			'lastname':request.POST['lastname'],
			'password':request.POST['password'],
		}
		data = urlencode(post_value).encode('utf-8')
		try:
			with urllib.request.urlopen("http://exp_host:8000/api/v1/user/create/",data) as url:
				content = url.read().decode('utf-8')
			user_response = json.loads(content)
		except HTTPError:
			return _error_response(request, 'unable to get http response from models api')
		if not user_response['ok']:
			return HttpResponse(user_response['error'])
		auth = user_response['resp']['authenticator']
		response = HttpResponseRedirect(reverse('Events'))
		response.set_cookie("auth",auth)
		return response
	user_form = UserForm()
	return render(request, 'register.html', {'user_form':user_form})

def login(request):
	if request.method == 'POST':
		if 'username' not in request.POST or \
			'password' not in request.POST:
			return HttpResponse('Required fields missing')
		username = request.POST['username']
		password = request.POST['password']
		post_value = {
			"username":username,
			"password":password,
		}
		data = urlencode(post_value).encode('utf-8')
		try:
			with urllib.request.urlopen("http://exp_host:8000/api/v1/user/login/", data) as url:
				content = url.read().decode("utf-8")
			login_response = json.loads(content)
		except HTTPError:
			return HttpResponse("unable to get http response from models api")
		if not login_response["ok"]:
			return HttpResponse(login_response["error"])
		auth = login_response["resp"]["authenticator"]
		response = HttpResponseRedirect(reverse('Events'))
		response.set_cookie("auth", auth)
		return response
	else:
		login_form = LoginForm()
	return render(request,'login.html',{'login_form':login_form})

def logout(request):
	response = HttpResponseRedirect(reverse('Events'))
	response.delete_cookie("auth")
	return response

def add_event(request):
	auth = request.COOKIES.get("auth")
	if not auth:
		return HttpResponseRedirect(reverse('Login'))
	if request.method == "POST":
		if 'name' not in request.POST or \
			'description' not in request.POST or \
			'start_time' not in request.POST or \
			'location' not in request.POST:
			return HttpResponse('missing required fields')
		post_value = {
			'authenticator':auth,
			'name':request.POST['name'],
			'description':request.POST['description'],
			'start_time':request.POST['start_time'],
			'location':request.POST['location'],
		}
		data = urlencode(post_value).encode('utf-8')
		try:
			with urllib.request.urlopen("http://exp_host:8000/api/v1/event/create/",data) as url:
				content = url.read().decode('utf-8')
			event_response = json.loads(content)
		except HTTPError:
			return HttpResponse("unable to get http response from models api")
		if not event_response['ok']:
			return HttpResponse(event_response['error'])
		event_id = event_response['resp']['event_id']
		return HttpResponseRedirect(reverse('Details',args=[event_id]))
	event_form = EventForm()
	return render(request, 'addevent.html', {'event_form':event_form})
# Create your views here.

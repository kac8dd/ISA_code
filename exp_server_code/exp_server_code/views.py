from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
import urllib
from urllib.parse import urlencode
from urllib.error import HTTPError 
import json

def index(request):
	return HttpResponse('This is the experience api.')

def create_user(request):
	"""
	method:POST
	api call: "http://exp_host:8000/api/v1/user/create/"
	input:username, firstname, lastname, password
	normal case return: {"resp": {"authenticator": "C/hVGf8L0+U43Pjc3hkjTkfNZKbWHHcayzvNZCJ/aVY="}, "ok": true}
	"""
	# edge case checking
	if request.method != 'POST':
		return _error_response(request, "must make POST request")
	if 'username' not in request.POST or \
		'firstname' not in request.POST or \
		'lastname' not in request.POST or \
		'password' not in request.POST:
		return _error_response(request, "missing required fields")
	# calling create_user
	post_value = {
		'username':request.POST['username'],
		'firstname':request.POST['firstname'],
		'lastname':request.POST['lastname'],
		'password':request.POST['password']
	}
	data = urlencode(post_value).encode('utf-8')
	try:
		with urllib.request.urlopen("http://models_host:8000/api/v1/create/user/",data) as url:
			content = url.read().decode('utf-8')
		user_response = json.loads(content)
	except HTTPError:
		return _error_response(request, 'unable to get http response from models api')
	# checking response
	if not user_response['ok']:
		return _error_response(request, user_response['error'])
	user_id = user_response['resp']['user_id']

	# get_user
	try:
		with urllib.request.urlopen("http://models_host:8000/api/v1/get/user/"+str(user_id)) as url:
			content = url.read().decode("utf-8")
		user_response = json.loads(content)
	except HTTPError:
		return _error_response("unable to get http response from models apiy")
	firstname = user_response["firstname"]
	lastname = user_response["lastname"]

	#calling create_authenticator()
	post_value = {
		'user_id':user_id
	}
	data = urlencode(post_value).encode('utf-8')
	try:
		with urllib.request.urlopen("http://models_host:8000/api/v1/create/authenticator/", data) as url:
			content = url.read().decode('utf-8')
		authenticator_response = json.loads(content)
	except HTTPError:
		return _error_response(request, 'unable to get http response from models api')
	if not authenticator_response["ok"]:
		return JsonResponse(authenticator_response)
	authenticator_response["resp"]["firstname"] = firstname
	authenticator_response["resp"]["lastname"] = lastname
	return JsonResponse(authenticator_response)

def logout(request):
	"""
	method:POST
	api call: "http://exp_host:8000/api/v1/user/logout/"
	input:authenticator
	normal case return:{"ok": true, "resp": {"userid": 32}}
	"""
	if request.method != 'POST':
		return _error_response(request, "must make POST request")
	if "authenticator" not in request.POST:
		return _error_response(request, "missing required fields")
	post_value = {
		"authenticator":request.POST["authenticator"]
	}

	data = urlencode(post_value).encode('utf-8')
	try:
		with urllib.request.urlopen("http://models_host:8000/api/v1/user/logout/",data) as url:
			content = url.read().decode('utf-8')
		logout_response = json.loads(content)
	except HTTPError:
		return _error_response(request, 'unable to get http response from models api')
	if not logout_response["ok"]:
		return _error_response(request, logout_response["error"])
	return JsonResponse(logout_response)

def login(request):
	"""
	method:POST
	api call: "http://exp_host:8000/api/v1/user/login/"
	input:username, password
	normal case return:{"resp": {"authenticator": "0SIZvopgP3D9H+YUm9aqBpC0brjrMbBwZg8jspJhj0g="}, "ok": true}
	"""
	if request.method != "POST":
		return _error_response(request, "must make POST request")
	if "username" not in request.POST or \
		"password" not in request.POST:
		return _error_response(request, "missing required fields")
	post_value = {
		"username":request.POST["username"],
		"password":request.POST["password"],
	}
	data = urlencode(post_value).encode("utf-8")
	try:
		with urllib.request.urlopen("http://models_host:8000/api/v1/user/validate/",data) as url:
			content = url.read().decode("utf-8")
		validate_response = json.loads(content)
	except HTTPError:
		return _error_response("unable to get http response from models apix")
	if not validate_response["ok"]:
		return JsonResponse(validate_response)
	user_id = validate_response["resp"]["user_id"]
	# get_user
	try:
		with urllib.request.urlopen("http://models_host:8000/api/v1/get/user/"+str(user_id)) as url:
			content = url.read().decode("utf-8")
		user_response = json.loads(content)
	except HTTPError:
		return _error_response("unable to get http response from models apiy")
	firstname = user_response["firstname"]
	lastname = user_response["lastname"]

	# create_authenticate
	post_value = {
		"user_id":user_id
	}

	data = urlencode(post_value).encode("utf-8")
	try:
		with urllib.request.urlopen("http://models_host:8000/api/v1/create/authenticator/",data) as url:
			content = url.read().decode("utf-8")
		authenticator_response = json.loads(content)
	except HTTPError:
		return _error_response(request, "unable to get http response from models apiz")
	if not authenticator_response["ok"]:
		return JsonResponse(authenticator_response)
	authenticator_response["resp"]["firstname"]=firstname
	authenticator_response["resp"]["lastname"]=lastname
	return JsonResponse(authenticator_response)

def create_event(request):
	"""
	method:POST
	api call: "http://exp_host:8000/api/v1/event/create/"
	input: authenticator, name, description, start_time, location
	normal case return: {"ok": true, "resp": {"event_id": 8}}
	"""
	if request.method != "POST":
		return _error_response(request, "must make post request")
	if "authenticator" not in request.POST or \
		"name" not in request.POST or \
		"description" not in request.POST or \
		"start_time" not in request.POST or \
		"location" not in request.POST:
		return _error_response(request, "missing required fields")
	post_value = {
		"authenticator" : request.POST["authenticator"]
	}
	data = urlencode(post_value).encode("utf-8")
	try:
		with urllib.request.urlopen("http://models_host:8000/api/v1/user/authenticate/",data) as url:
			content = url.read().decode("utf-8")
		authenticate_response = json.loads(content)
	except HTTPError:
		return _error_response(request, "unable to get http response from models api")
	if not authenticate_response["ok"]:
		return JsonResponse(authenticate_response)
	user_id = authenticate_response["resp"]["user_id"]
	post_value = {
		"name" : request.POST["name"],
		"description" : request.POST["description"],
		"location" : request.POST["location"],
		"start_time" : request.POST["start_time"],
		"creator_id" : user_id
	}
	data = urlencode(post_value).encode("utf-8")
	try:
		with urllib.request.urlopen("http://models_host:8000/api/v1/create/event/",data) as url:
			content = url.read().decode("utf-8")
		event_response = json.loads(content)
	except HTTPError:
		return _error_response(request, 'unable to get http response from models api')
	return JsonResponse(event_response)

def _error_response(request,error_msg):
    return JsonResponse({'ok': False, 'error': error_msg})

def _success_response(request,resp=None):
    if resp:
        return JsonResponse({'ok': True, 'resp': resp})
    else:
        return JsonResponse({'ok': True})
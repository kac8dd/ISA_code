from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
import urllib
from urllib.parse import urlencode
from urllib.error import HTTPError 
import json

def index(request):
	return HttpResponse('This is the experience api.')

def create_user(request):
	"""
	create user with the post fields in the database
	create authenticator for that user
	return that authenticator in JSON with key "authenticator"
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
	# checking response
	if not authenticator_response['ok']:
		return _error_response(request, authenticator_response['error'])
	return JsonResponse(authenticator_response["resp"])

def authenticate_user(request):
	# edge case checking
	if request.method != 'POST':
		return _error_response(request, "must make POST request")
	if 'authenticator' not in request.POST:
		return _error_response(request, "missing required fields")
	# calling authenticate()
	post_value = {
		"authenticator":request.POST['authenticator']
	}
	data = urlencode(post_value).encode('utf-8')
	try:
		with urllib.request.urlopen("http://models_host:8000/api/v1/user/authenticate/", data) as url:
			content = url.read().decode('utf-8')
		authenticate_response = json.loads(content)
	except HTTPError:
		return _error_response(request, 'unable to get http response from models api')
	# checking response
	if not authenticate_response['ok']:
		return _error_response(request, authenticate_response['error'])
	return JsonResponse(authenticate_response)

# def logout(request):

def _error_response(request,error_msg):
    return JsonResponse({'ok': False, 'error': error_msg})

def _success_response(request,resp=None):
    if resp:
        return JsonResponse({'ok': True, 'resp': resp})
    else:
        return JsonResponse({'ok': True})
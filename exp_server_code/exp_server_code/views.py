from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
import urllib
from urllib.parse import urlencode

def index(request):
	return HttpResponse('This is the experience api.')

def create_user(request):
	if request.method != 'POST':
		return _error_response(request, "must make POST request")
	if 'username' not in request.POST or \
		'firstname' not in request.POST or \
		'lastname' not in request.POST or \
		'password' not in request.POST:
		return _error_response(request, "missing required fields")
	post_value = {
		'username':request.POST['username'],
		'firstname':request.POST['firstname'],
		'lastname':request.POST['lastname'],
		'password':request.POST['password']
	}
	# try:
	data = urlencode(post_value).encode('utf-8')
	with urllib.request.urlopen("http://models_host:8000/api/v1/create/user/",data) as url:
		content = url.read().decode('utf-8')
	# except:
	# 	return _error_response(request,"error")
	return HttpResponse(content)


def _error_response(request,error_msg):
    return JsonResponse({'ok': False, 'error': error_msg})

def _success_response(request,resp=None):
    if resp:
        return JsonResponse({'ok': True, 'resp': resp})
    else:
        return JsonResponse({'ok': True})
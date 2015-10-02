from django.shortcuts import render

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

import urllib.request 
from urllib.error import HTTPError

import json

#these are not front faceing POSTs so we don't need csrf tokens
from django.views.decorators.csrf import csrf_exempt


def index(request):
	num = 5	
	try:
		#make api call to models layer for the latest events
		with urllib.request.urlopen("http://models_host:8000/api/v1/get/latest/"+str(num)+"/") as url:
			#decode the response
			str_response = url.readall().decode('utf-8') 
			
			#convert into json/python dictionary
			latest_events_json = json.loads(str_response) 
			
			#get the information about the creator of each event and craft a response	
			x = 0
			response = {}
	
			while x < num:
				current_event = latest_events_json[str(x)] 
				str_response = urllib.request.urlopen("http://models_host:8000/api/v1/get/user/"+str(current_event['creator'])+"/").readall().decode('utf-8') 
				current_creator= json.loads(str_response)
				response[str(current_event)] = str(current_creator)
				x=x+1	
	except HTTPError:
		return _error_response(request, 'unable to get http response from database')

	return JsonResponse(response)


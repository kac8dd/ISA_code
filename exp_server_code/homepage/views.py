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
    try:
        with urllib.request.urlopen("http://models_host:8000/api/v1/get/latest/5/") as url:
            latest_events_json = url.read()
        response = json.loads(latest_events_json.decode('utf-8'))

        # for each event in our response, replace 'creator': 'id' with 'creator': {name: bob, ...}
        for event_id in response:
            creator_id = str(response[event_id]['creator'])
            with urllib.request.urlopen("http://models_host:8000/api/v1/get/user/"+creator_id+"/") as url:
                event_creator_json = url.read()
            user_response = json.loads(event_creator_json.decode('utf-8'))
            response[event_id]['creator'] = user_response

    except HTTPError:
        return _error_response(request, 'unable to get http response from database')
    return JsonResponse(response)

def _error_response(request,error_msg):
    return JsonResponse({'ok': False, 'error': error_msg})
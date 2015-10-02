from django.http import HttpResponse
from django.shortcuts import render

import urllib.request 
import json
from urllib.error import HTTPError

def index(request):
    try:
        with urllib.request.urlopen("http://exp_host:8000/api/v1/home/") as url:
            latest_events_json = url.read()
        jsonstring = json.loads(latest_events_json.decode('utf-8'))
        resp = json.loads(jsonstring['resp'])
        events = []
        for key in resp:
            events.append(resp[key])
    except HTTPError:
        events = "read from exp_host failed"
    return render(request, 'eventlist.html', {
        'events': events,
    })

def details(request, event_id):
    url = "http://exp_host:8000/api/v1/view_event/event=" + event_id + "/"
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

def addevent(request):
    return render(request, 'addevent.html', {
        'text': "Add events here eventually",
    })
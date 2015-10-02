from django.shortcuts import render

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

import urllib.request 
import json

# Create your views here.
def index(request):
	
	str_response = urllib.request.urlopen("http://exp_host:8000/api/v1/home/").readall().decode('utf-8')
	json_fields = json.loads(str_response)
	d = json.dumps(json_fields)
	return render_to_response('index.html',{'dict':d})


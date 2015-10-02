from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse

def index(request):
	return HttpResponse('This is the experience api.')
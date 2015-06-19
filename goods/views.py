from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.conf import settings
# Create your views here.

def test(requst):
	a = "It is worked"
       
	return HttpResponse(a)

def index(request):
    args ={}
    args.update(csrf(request))
    return render(request, "web/index.html", args)

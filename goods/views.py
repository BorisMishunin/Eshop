from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.conf import settings
from models import Wares
# Create your views here.

def test(requst):
	a = "It is worked"
       
	return HttpResponse(a)

def index(request):
    wares_list = Wares.objects.order_by('Code')
    args ={}
    args.update(csrf(request))
    args['wares'] = wares_list
    return render(request, "web/index.html", args)

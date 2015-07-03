# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.conf import settings
from models import Wares, WaresProperties


# Create your views here.

def index(request):
    wares_list = Wares.objects.order_by('Code')
    args ={}
    args.update(csrf(request))
    args['wares'] = wares_list
    return render(request, "web/index.html", args)


def good_card(request, Wares_id):
	args = {}
	args.update(csrf(request))
	args['wares'] = Wares.objects.get(id=Wares_id)
	args['properties'] = WaresProperties.objects.filter(Ware_id=Wares_id)
	return render_to_response('good_card.html', args)
	

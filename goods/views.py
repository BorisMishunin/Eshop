from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test(requst):
	a = "It is worked"
       
	return HttpResponse(a)


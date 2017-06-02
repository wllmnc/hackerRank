# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import JsonResponse
import random
from .admin_ele import Admin 

admin=0
# Create your views here.
def hello(request):
    return HttpResponse('hello world')

# view to reach the index.html
class HomePageView(TemplateView):
    template_name = "index.html"

# view to get the elevator status 
def get_elevator_status(request):
        id_elevator=request.GET.get('elevator', None)
	return JsonResponse(get_elevatorStatus(id_elevator),safe=False)

# view to ask for a service of elevator
def ask_elevator(request):
	id_floor=int(request.GET.get('floor', None))
	up_down=request.GET.get('up_down', None)
        up_down= 1 if up_down=="1" else 0
	return JsonResponse(get_elevator_toflor(id_floor,up_down),safe=False)

# method to return an answer to the view ask elevator	
def get_elevator_toflor(id_floor, up_down):
	elevator_num=admin.ask_resources(id_floor,up_down)
	ans={
	'Floor':id_floor,
	'Elevator':elevator_num
	}
	return ans
# method bridge between viewn and admin
def set_elevator_toflor(id_elevator,id_floor):
        admin.set_destination_elevator(id_elevator,id_floor)
        ans={
        'Floor':id_floor,
        'Elevator':id_elevator
        }
        return ans

# method bridge between viewn and admin 
def get_elevatorStatus(id_elevator):
	res=admin.get_information_elevator(int(id_elevator)-1)
        ans={
            'Elevator':res[0],
            'Current_floor':res[1],
            'is_openDoors':res[2],
	    'Sense':res[3]
        }
        return ans

#view to ser a req for a single one elevetor 
def set_elevator_req(request):
	id_elevator=int(request.GET.get('elevator', None))
        id_floor=int(request.GET.get('floor', None))
        return JsonResponse(set_elevator_toflor(id_elevator,id_floor), safe=False)	

#view to initialize the admin object
def init_admin(request):
	#create intance of admin with n and m values
        n=request.GET.get('n', None)
        m=request.GET.get('m', None)
	global admin
	admin=Admin(int(n),int(m))
	return JsonResponse({'Operation':1})


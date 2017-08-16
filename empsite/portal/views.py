from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from .models import Employee

def index(request):
    name_list = Employee.objects.all()
    output = ", ".join(name.emp_name for name in name_list)
    return HttpResponse('output')

def details(request, id):
    return HttpResponse('Employee name: %s' % id)

def points(request, id):
    return HttpResponse('Employe name results: %s' % id)




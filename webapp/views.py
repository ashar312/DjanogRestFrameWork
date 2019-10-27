from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . Serializers import employeesSerializers
from . forms import Employeesform


def post_create(request):
    form = Employeesform(request.POST or None)
    print(request.POST)
    if(form.is_valid()):
        instance = form.save(commit = False)
        print(form.cleaned_data.get('firstname'))
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form' : form
    }
    return render(request, 'employees_form.html',context)

def post_get(request, id=None):
    instance = get_object_or_404(employees,id = id)
    context = {
        'firstname' : instance.firstname,
        'instance' : instance
    }
    return render(request, 'employeesDetail.html',context)

def post_list(request):
    queryset = employees.objects.all()
    instance = get_object_or_404(employees,id = 2)
    context = {
        'object_list' : queryset,
        'title' : 'LIST'
    }
    return render(request, 'index.html',context)

def post_update(request, id=None):
    instance = get_object_or_404(employees,id = id)
    form = Employeesform(request.POST or None,instance=instance)
    if(form.is_valid()):
        instance = form.save(commit = False)
        print(form.cleaned_data.get('firstname'))
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'firstname' : instance.firstname,
        'instance' : instance,
        'form' : form
    }
    return render(request, 'employees_form.html',context)


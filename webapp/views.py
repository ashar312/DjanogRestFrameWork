from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . Serializers import employeesSerializers
from . forms import Employeesform
from django.core.paginator import Paginator
from django.shortcuts import render


def post_create(request):
    form = Employeesform(request.POST or None, request.FILES or None)
    print(request.POST)
    if(form.is_valid()):
        instance = form.save(commit = False)
        print(form.cleaned_data.get('firstname'))
        instance.save()
        messages.success(request,"Success")
       # return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,"Fail")
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
    paginator = Paginator(queryset, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {
        'object_list' : contacts,
        'title' : 'LIST'
    }
    return render(request, 'base.html',context)





def post_update(request, id=None):
    instance = get_object_or_404(employees,id = id)
    form = Employeesform(request.POST or None, request.FILES or None ,instance=instance)
    if(form.is_valid()):
        instance = form.save(commit = False)
        print(form.cleaned_data.get('firstname'))
        instance.save()
        messages.success("Item Saved")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'firstname' : instance.firstname,
        'instance' : instance,
        'form' : form
    }
    return render(request, 'employees_form.html',context)

def post_delete(request, id=None):
    instance = get_object_or_404(employees,id = id)
    instance.delete()
    messages.success(request,"Successfully deleted")
    return redirect('list')


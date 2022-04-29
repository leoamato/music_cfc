#Imports
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def homepage (request):
    return render (request, 'homepage.html', {})

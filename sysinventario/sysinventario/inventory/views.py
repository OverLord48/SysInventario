from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, CreateView
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.urls import reverse_lazy
from .models import *
from .form import *

# Create your views here.

def home_inventory(request):
    return HttpResponse("<h1>Hola</h1>")

def home(request):
    return HttpResponse("<h1>Hola home</h1>")

class CategoryCreateView(CreateView):
    model = Categories
    form_class = CategoryForm
    # template_name = 'vista_create' #aun falta definir que implementaremos
    # success_url = reverse_lazy('inventory:name_route')
    
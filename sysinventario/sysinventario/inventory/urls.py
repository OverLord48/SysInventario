from django.urls import path
from .views import *

app_name = 'inventory'

urlpatterns = [
    path('category/', home_inventory, name="home"),
    path('categort/create/', CategoryCreateView.as_view(), name="createCat"),
]
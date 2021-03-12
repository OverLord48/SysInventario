from django.forms import ModelForm
from .models import *
class CategoryForm(ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'
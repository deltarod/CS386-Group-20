from django.shortcuts import render
from .models import School

# Create your views here.

def index(request):
    return render(request, 'School/schoolIndex.html')

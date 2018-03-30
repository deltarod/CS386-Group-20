from django.shortcuts import render
from django.db.models import Q
# Create your views here.


def index(request):
    return render( request, 'homepage/header.html')

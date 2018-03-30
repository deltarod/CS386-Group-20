from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render( request, 'homepage/homepage.html')


def account(request):
    return render( request, 'Users/account.html')
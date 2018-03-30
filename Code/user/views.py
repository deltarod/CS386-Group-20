from django.shortcuts import render
from django.contrib.auth.models import User

def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'Users/user.html', {"user":user})
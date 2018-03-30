from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', auth_views.login, {"template_name": "signin/signin.html"}, name="signin")
]

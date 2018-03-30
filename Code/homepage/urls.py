from django.conf.urls import include, re_path
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    re_path('^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="homepage/homepage.html")),
    re_path(r'^(?P<pk>\d+)\/?$', DetailView.as_view(model=Post, template_name="homepage/post.html")),
    re_path('logout/', auth_view.logout, {'template_name': 'homepage/logout.html'}, name='logout'),
    re_path('account/', views.account, name="account")
]

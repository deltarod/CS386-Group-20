from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    url('^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="homepage/homepage.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name="homepage/post.html")),
    url('logout/', auth_view.logout, {'template_name': 'homepage/logout.html'}, name='logout'),
    url('account/', views.account, name="account")
]

from django.conf.urls import include, re_path
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib.auth import views as auth_view
from . import views
from .models import School

urlpatterns = [
    re_path('^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                                   template_name="homepage/homepage.html")),

    re_path(r'^(?P<pk>\d+)\/?$', DetailView.as_view(model=Post, template_name="homepage/post.html")),
    re_path('logout/', auth_view.logout, {'template_name': 'homepage/logout.html'}, name='logout'),
    re_path('account/$', views.account, name="account"),

    # edit profile
    re_path('account/edit/$', views.edit_account, name="edit_account"),

    # school
    re_path('school/$',ListView.as_view(queryset=School.objects.all()
                              .order_by("schoolName"), template_name="School/schoolIndex.html")),

    re_path(r'^school/(?P<pk>\d+)\/?$', DetailView.as_view(
        model=School,
        template_name="School/school.html")),

    re_path('School/joinSchool', views.addToSchool),

    re_path('School/leaveSchool', views.removeFromSchool),

    # signup
    re_path(r'^register/$', views.UserFormView.as_view(), name="register"),

    # signin
    re_path(r'^signin/$', auth_view.login, {"template_name": "signin/signin.html"}, name="signin"),

    # user
    re_path(r'user/(?P<username>[a-zA-Z0-9]+)/$', views.get_user_profile),

    # search
    re_path('search/', views.search, name="search")




]

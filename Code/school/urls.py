from .models import School
from django.conf.urls import url, include, re_path
from django.views.generic import ListView, DetailView
from . import views


urlpatterns = [
    re_path('^$',ListView.as_view(queryset=School.objects.all()
                              .order_by("schoolName"), template_name="School/schoolIndex.html")),
    re_path(r'^(?P<pk>\d+)\/?$', DetailView.as_view(
        model=School,
        template_name="School/school.html")),
]

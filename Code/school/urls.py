from .models import School
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView


urlpatterns = [
    url('^$',ListView.as_view(queryset=School.objects.all().order_by("schoolName"), template_name="School/schoolIndex.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=School, template_name="School/school.html"))
]

from django.shortcuts import render
from .models import School

# Create your views here.

def index(request):
    return render(request, 'School/schoolIndex.html')

def getSchool(request, School):
    school = School.objects.get(schoolName=School)
    return render(request, 'School/school.html', {"school":school})
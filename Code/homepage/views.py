from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth.models import User
from django.db.models import Q
from .models import School, Profile
# Create your views here.


def index(request):
    return render( request, 'homepage/homepage.html')


def account(request):
    return render( request, 'Users/account.html')

class UserFormView(View):
    form_class = UserForm
    template_name = 'signup/signup.html'

    # blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']

            password = form.cleaned_data['password']

            user.set_password(password)

            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)

                    return redirect('/')



        return render(request, self.template_name, {'form': form})


def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'Users/user.html', {"user":user})


def signin(request):
    return render(request, 'signin/signin.html')


def search(request):
    template = 'search/search.html'

    query = request.GET.get('q')

    resultsUser = User.objects.filter(Q(username__icontains=query))

    resultsCollege = School.objects.filter(Q(schoolName__icontains=query) | Q(location__icontains=query))

    return render(request, template, {"user": resultsUser, "college": resultsCollege})


def addToSchool(request):
    if request.method=="GET":
        schoolID = request.GET.get('school')
        if not schoolID:
            return render(request, '/')

        else:
            school = School.objects.get(pk=schoolID)

            request.user.profile.college = school

            request.user.save()

            return render(request, "School/schoolJoin.html", {"school":school})


def removeFromSchool(request):
    if request.method=="GET":
        schoolID = request.GET.get('school')
        if not schoolID:
            return render(request, '/')

        else:
            school = School.objects.get(pk=schoolID)

            request.user.profile.college = None

            request.user.save()

            return render(request, "School/schoolLeave.html", {"school":school})


from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


@login_required()
def index(request):
    return render(request, 'index.html')


def logout_view(request):
    logout(request)
    return render(request, 'registration/login.html')


@login_required()
def hello(request):
    return render(request, 'hello.html')

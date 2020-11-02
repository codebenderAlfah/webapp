from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse('Hello from myapp')
    return render(request, 'index.html')


def search(request):
    # return HttpResponse('Hello from myapp')
    return render(request, 'search.html')


def history(request):
    # return HttpResponse('Hello from myapp')
    return render(request, 'history.html')


def profile(request):
    # return HttpResponse('Hello from myapp')
    return render(request, 'profile.html')


def contact(request):
    # return HttpResponse('Hello from myapp')
    return render(request, 'contact.html')

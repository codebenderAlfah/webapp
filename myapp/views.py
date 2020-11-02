from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse('Hello from myapp')
    return render(request,'index.html')

def search(request):
    #return HttpResponse('Hello from myapp')
    return render(request,'event/search.html')

def history(request):
    #return HttpResponse('Hello from myapp')
    return render(request,'event/history.html')

def profile(request):
    #return HttpResponse('Hello from myapp')
    return render(request,'event/profile.html')

def contact(request):
    #return HttpResponse('Hello from myapp')
    return render(request,'event/contact.html')
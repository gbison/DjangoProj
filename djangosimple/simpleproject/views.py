from django.http import HttpResponse
from django.shortcuts import render


def homepage (request):
    #return HttpResponse("Home Page")
    return render(request, 'home.html')

def aboutpage(request):
    return render(request, 'about.html', {'name':'Bryan'})

def contactpage(request):
    return render(request, 'contact.html')
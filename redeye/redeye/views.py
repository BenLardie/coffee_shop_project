from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render




def home_page(request):
    html = render(request, 'index.html')
    return HttpResponse(html)

def root(request):
    return HttpResponseRedirect('home')

def about(request):
    html = render(request, 'about.html')
    return HttpResponse(html)

def menu(request):
    html = render(request, 'menu.html')
    return HttpResponse(html)

def location(request):
    html = render(request, 'location.html')
    return HttpResponse(html)
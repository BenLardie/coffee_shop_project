from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from redeye.models import Menu, Item



def home_page(request):
    html = render(request, 'index.html')
    return HttpResponse(html)

def root(request):
    return HttpResponseRedirect('home')

def about(request):
    html = render(request, 'about.html')
    return HttpResponse(html)

def menu(request):
    context = {'menu' : Menu.objects.all(), 'item' : Item.objects.all}
    html = render(request, 'menu.html', context)
    return HttpResponse(html)

def location(request):
    html = render(request, 'location.html')
    return HttpResponse(html)
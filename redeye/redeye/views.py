from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render




def home_page(request):
    html = render(request, 'index.html')
    return HttpResponse(html)

def root(request):
    return HttpResponseRedirect('home')
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'homepage.html')

def about(request):
    #return HttpResponse("Hello, World, You are in the about page ")
    return render(request, 'about.html')


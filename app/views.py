from django.shortcuts import render
from django.http import HttpResponse

def frontpage(request):
    return HttpResponse('<p2>Welcome to our awesome application!</p2>') 

def sidebar(request):
    return render(request, "components/sidebar.html")
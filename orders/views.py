from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def acerca(request):
    return render(request, "acerca.html")



def menu(request):
    return render(request, "menu.html")


def contacto(request):
    return render(request, "contacto.html")

def login(request):
    return render(request, "login.html")

def registrar(request):
    return render(request, "registrar.html")
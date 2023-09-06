from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("PORTADA")
def about(request):
    return HttpResponse("ACERCA DE")

def services(request):
    return HttpResponse("SERVICIOS")

def store(request):
    return HttpResponse("TIENDA")

def contact(request):
    return HttpResponse("CONTACTO")

def blog(request):
    return HttpResponse("BLOG")

def sample(request):
    return HttpResponse("EJEMPLO")



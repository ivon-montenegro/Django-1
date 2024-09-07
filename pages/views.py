from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.

def Home(request):
    return render(request,"Template_Hola")

def Hola(request):
    return HttpResponse("Hola")

class HomePageView(TemplateView):
    template_name="home.html"
    

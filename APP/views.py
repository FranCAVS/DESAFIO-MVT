from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from APP.models import Familia
from django.template import loader
# Create your views here.

def saludo(request):
    return HttpResponse("HOLA PA")

def mostrar_template(request):
    return render(request, "APP/index.html")

def listar_familias(request):
    context={}
    context["familias"] = Familia.objects.all()
    return render(request, "APP/lista_familia.html", context)

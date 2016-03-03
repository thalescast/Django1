from django.shortcuts import render
from django.http import HttpResponse

def views_1(request):

#Sem o request no render nao funciona
    return render(request, "templateForm.html")


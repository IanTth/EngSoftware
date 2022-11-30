from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def entrar(request):
    return render(request,'entrar.html')
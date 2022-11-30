from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def entrar(request):
    return render(request,'entrar.html')

def home(request):
    return render(request,'home.html')



def ajuda(request):
    return render(request,'ajuda.html')

def camera(request):
    return render(request,'camera.html')

def comp(request):
    return render(request,'comparativo.html')

def conf(request):
    return render(request,'configuracoes.html')

def dash(request):
    return render(request,'dashboard.html')

def inf(request):
    return render(request,'informacoes.html')

def monit(request):
    return render(request,'monitoramento.html')

def nponto(request):
    return render(request,'novo-ponto.html')
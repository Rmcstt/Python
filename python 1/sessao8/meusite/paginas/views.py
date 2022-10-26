from django.shortcuts import render

# Create your views here.
def index(request):
  return request('paginas/index.html')


def sobre(request):
  return request('paginas/sobre.html')
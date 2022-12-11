from django.shortcuts import render
from .models import Cliente
# Create your views here.

def listar_clientes(request):
    clientes = clientes.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes':clientes})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Estados

def listar_estados(request):
    estados = Estados.objects.all()
    return render(request, 'listarestado.html', {'estados': estados})

def cadastrar_estado(request):
   if request.method == 'POST':
      nome = request.POST['nome']
      sigla = request.POST['sigla']
      Estados.objects.create(nome=nome, sigla=sigla)
      return redirect('listar_estados')
   return render(request, 'formestado.html')

def editar_estado(request, id):
    estado = get_object_or_404(Estados, id=id)
    if request.method == "POST":
        estado.nome = request.POST['nome']
        estado.sigla = request.POST['sigla']
        estado.save()
        return redirect('listar_estados')
    return render(request, 'formestado.html', {'estado': estado})

def excluir_estado(request, id):
    estado = get_object_or_404(Estados, id=id)
    if request.method == "POST":
        estado.delete()
        return redirect('listar_estados')
    return render(request, 'confirmar_exclusaoestado.html', {'estado': estado})

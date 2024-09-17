from django.shortcuts import get_object_or_404, render, redirect
from cidades.forms import CidadeForm
from cidades.models import Cidades

def listar_cidades(request):
    cidades = Cidades.objects.all()
    return render(request, 'listarcidade.html', {'cidades': cidades})

def cadastrar_cidade(request):
    if request.method == "POST":
        form = CidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cidades')
    else:
        form = CidadeForm()
    return render(request, 'formcidade.html', {'form': form})

def editar_cidade(request, id):
    cidade = get_object_or_404(Cidades, id=id)
    if request.method == "POST":
        form = CidadeForm(request.POST, instance=cidade)
        if form.is_valid():
            form.save()
            return redirect('listar_cidades')
    else:
        form = CidadeForm(instance=cidade)
    return render(request, 'formcidade.html', {'form': form})

def excluir_cidade(request, id):
    cidade = get_object_or_404(Cidades, id=id)
    if request.method == "POST":
        cidade.delete()
        return redirect('listar_cidades')
    return render(request, 'confirmar_ex_cidade.html', {'cidade': cidade})

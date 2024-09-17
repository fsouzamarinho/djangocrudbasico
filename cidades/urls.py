from django.urls import path
from cidades.views import listar_cidades, cadastrar_cidade, editar_cidade, excluir_cidade


urlpatterns = [
    path('', listar_cidades, name='listar_cidades'),
    path('cidades/cadastrar/', cadastrar_cidade, name='cadastrar_cidade'),
    path('cidades/editar/<int:id>/', editar_cidade, name='editar_cidade'),
    path('cidades/excluir/<int:id>/', excluir_cidade, name='excluir_cidade'),
]

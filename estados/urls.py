from django.urls import path
from .views import listar_estados, cadastrar_estado, editar_estado, excluir_estado

urlpatterns = [
    path('', listar_estados, name='listar_estados'),
    path('cadastrar/', cadastrar_estado, name='cadastrar_estado'),
    path('editar/<int:id>/', editar_estado, name='editar_estado'),
    path('excluir/<int:id>/', excluir_estado, name='excluir_estado'),
]

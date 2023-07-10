from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_produtos/', views.cadastrar_produtos, name='cadastrar_produtos'),
    path('pesquisar_produtos/', views.pesquisar_produtos, name='pesquisar_produtos'),
    path('detalhes_produtos/<int:id>', views.detalhes_produtos, name='detalhes_produtos'),
    path('deletar_produtos/<int:id>', views.deletar_produtos, name='deletar_produtos'),
    path('editar_produtos/<int:id>', views.editar_produtos, name='editar_produtos'),
    path('busca/', views.search, name='busca')
] 

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('recarregar_comanda/<int:id>', views.recarregar_comanda, name='recarregar_comanda'),
    path('detalhes_comanda/<int:id>', views.detalhes_comanda, name='detalhes_comanda'),
    path('pesquisar_comanda/', views.pesquisar_comanda, name='pesquisar_comanda'),
    path('ferramentas/', views.ferramentas, name='ferramentas'),
    path('sobre/', views.sobre, name='sobre'),
    path('busca_id/', views.search, name='busca_id'),
    path('pesquisar_comanda_consumo/', views.pesquisar_comanda_consumo, name='pesquisar_comanda_consumo'),
    path('cliente/<int:cliente_id>/comanda/<int:comanda_id>/produto/<int:produto_id>/consumo/<int:quantidade>/', views.realizar_consumo, name='realizar_consumo'),
    path('search_id_consumo/', views.search_id_consumo, name='search_id_consumo'),
    path('sucesso', views.sucesso, name='sucesso')

]
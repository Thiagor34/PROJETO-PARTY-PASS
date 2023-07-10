from django.urls import path, include
from . import views


urlpatterns = [
    # path("", views.index, name="home"),
    path("cadastrar_cliente/", views.cadastrar_cliente, name="cadastrar_cliente"),
    path("pesquisar_cliente/", views.pesquisar_cliente, name="pesquisar_cliente"),
    path("redirecionar_recarregar_comanda/<int:id>/", views.recarregar_comanda, name="redirecionar_recarregar_comanda"),
    ]

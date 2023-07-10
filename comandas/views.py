from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import Comandas
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from clientes.models import Clientes
from datetime import date
from produtos.models import Produtos
from django.http import JsonResponse
from django.contrib import messages



def index(request):
    return render(request, "pages/index.html")


def ferramentas(request):
    return render(request, "pages/ferramentas.html")


def sobre(request):
    return render(request, "pages/sobre.html")


@login_required(redirect_field_name="login")
def search(request):
    comandas = Comandas.objects.filter(usuario_id=request.user.id).order_by("-id")
    q = request.GET.get("search")
    cliente = None
    comanda = None
    if q:
        if q.isdigit():
            cliente = Clientes.objects.filter(id=q).first()
            comanda = Comandas.objects.filter(id=q).first()
            if cliente or comanda:
                return redirect("recarregar_comanda", id=q)
            else:
                messages.error(request, "ID inválido.")
                return redirect("pesquisar_comanda")
        else:
            messages.error(request, "O campo de pesquisa deve ser um número.")
            return redirect("pesquisar_comanda")
    else:
        messages.error(request, "O campo de pesquisa não pode estar vazio.")
        return redirect("pesquisar_comanda")

@login_required(redirect_field_name="login")
def pesquisar_comanda(request):
    comandas = Comandas.objects.filter(usuario_id=request.user.id).order_by("-id")
    return render(request, "pages/pesquisar_comanda.html", {"comandas": comandas})


@login_required(redirect_field_name="login")
def detalhes_comanda(request, id):
    comandas = Comandas.objects.filter(usuario_id=request.user.id).order_by("-id")
    cliente = get_object_or_404(Clientes, id=id)
    return render(
        request,
        "pages/recarregar_comandas.html",
        {"cliente": cliente, "comandas": comandas},
    )


@login_required(redirect_field_name="login")
def recarregar_comanda(request, id):
    comandas = Comandas.objects.filter(usuario_id=request.user.id).order_by("-id")
    cliente = get_object_or_404(Clientes, id=id)
    comanda = Comandas.objects.filter(cliente_id=id).first()

    if request.method == "POST":
        nome = request.POST.get("nome")
        saldo = request.POST.get("saldo")
        valor_comanda = request.POST.get("valor_comanda")
        forma_pagamento = request.POST.get("forma_pagamento")
        cliente.nome = nome
        comanda.saldo = saldo
        comanda.ultima_recarga = date.today()

        if valor_comanda.isdigit():
            valor_comanda = valor_comanda.replace(",", ".")
            comanda.saldo = comanda.saldo.replace(",", ".")
            valor_comanda = float(valor_comanda)
            comanda.saldo = (
                float(comanda.saldo) + valor_comanda
            )  # Adiciona o valor da recarga ao saldo existente
            comanda.forma_pagamento = forma_pagamento

        cliente.save()
        comanda.save()
        return redirect("home")

    else:
        return render(
            request,
            "pages/recarregar_comanda.html",
            {"cliente": cliente, "comanda": comanda, "comandas": comandas},
        )


@login_required(redirect_field_name="login")
def pesquisar_comanda_consumo(request):
    comandas = Comandas.objects.filter(usuario_id=request.user.id).order_by("-id")
    produtos = Produtos.objects.all()
    return render(
        request, "pages/pesquisar_comanda_consumo.html", {"comandas": comandas, "produtos": produtos}
    )




def search_id_consumo(request):
    q = request.GET.get("busca_com")
    produto_id = request.GET.get("produto_id")
    quantidade = request.GET.get("quantidade")

    if q and produto_id and quantidade:
        try:
            cliente = Clientes.objects.get(id=q)
            comanda = Comandas.objects.get(cliente=cliente, id=q)
        except Clientes.DoesNotExist:
            cliente = None
            comanda = None
        except Comandas.DoesNotExist:
            comanda = None

        if cliente and comanda:
            # Redirecionar para realizar_consumo
            return redirect(
                "realizar_consumo",
                cliente_id=cliente.id,
                comanda_id=comanda.id,
                produto_id=produto_id,
                quantidade=quantidade,
            )

    # Cliente ou comanda inválidos, exibir mensagem de erro
    messages.error(request, "Cliente ou comanda inválidos.")

    # Redirecionar para pesquisar_comanda_consumo com mensagem de erro
    return redirect('pesquisar_comanda_consumo')





def realizar_consumo(request, cliente_id, comanda_id, produto_id, quantidade):
    # Verificar se o cliente, comanda e produto existem
    cliente = get_object_or_404(Clientes, pk=cliente_id)
    comanda = get_object_or_404(Comandas, pk=comanda_id, cliente=cliente)
    produto = get_object_or_404(Produtos, pk=produto_id)

    try:
        quantidade = int(quantidade)

        if quantidade <= 0:
            messages.error(request, message='Quantidade inválida')
            return redirect('pesquisar_comanda_consumo')

        if comanda.saldo >= produto.valor * quantidade:

            valor_total = produto.valor * quantidade

            comanda.saldo -= valor_total
            comanda.save()

            return redirect('sucesso')

        messages.error(request, message='Saldo insuficiente')
        return redirect('pesquisar_comanda_consumo')
        

    except ValueError:
        messages.error(request, message='Quantidade inválida')
        return redirect('pesquisar_comanda_consumo')
        


def busca_prod(request):
    busca_prod_id = request.GET.get("busca_prod")
    produto = get_object_or_404(Produtos, id=busca_prod_id)
    data = {"id": produto.id, "nome": produto.nome, "valor": produto.valor}
    return JsonResponse(data, safe=False)

def sucesso(request):
    return render(request, "pages/sucesso.html")
from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from .models import Clientes
from comandas.models import Comandas
from datetime import date
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from comandas.views import recarregar_comanda

@login_required(redirect_field_name="login")
def cadastrar_cliente(request):
    comandas = Comandas.objects.filter(usuario_id=request.user.id).order_by("-id")
    if request.method == "POST":
        nome = request.POST.get("nome")
        cpf = request.POST.get("cpf")
        telefone = request.POST.get("telefone")
        if not nome or nome.isspace():
            messages.error(request, "O campo Nome é obrigatório.")
            return redirect("cadastrar_cliente")  
        elif len(nome) < 3:
            messages.error(request, "O nome deve ter pelo menos 3 caracteres.")
            return redirect("cadastrar_cliente") 
        if not telefone or telefone.isspace():
            messages.error(request, "O campo Telefone é obrigatório.")
            return redirect("cadastrar_cliente")  
        if not cpf or cpf.isspace():
            messages.error(request, "O campo CPF é obrigatório.")
            return redirect("cadastrar_cliente")  
        

        if Clientes.objects.filter(cpf=cpf).exists():
            messages.error(request, "CPF já cadastrado.")
            return redirect("cadastrar_cliente")  
        
        email = request.POST.get("email")
        data_nascimento = request.POST.get("data_nascimento")
        endereco = request.POST.get("endereco")
        saldo = request.POST.get("saldo")
        if saldo:
            saldo = float(saldo)
        else:
            saldo = 0.00

        novo_cliente = Clientes(
            nome=nome,
            cpf=cpf,
            telefone=telefone,
            email=email,
            data_nascimento=data_nascimento,
            endereco=endereco,
        )

        nova_comanda = Comandas(
            cliente=novo_cliente, ultima_recarga=date.today(), saldo=saldo, usuario_id=request.user.id
        )

        novo_cliente.save()
        nova_comanda.save()

        messages.success(request, "Cliente cadastrado com sucesso!")
        return redirect("home")
    else:
        return render(request, "pages/cadastrar_cliente.html", {"comandas": comandas})



@login_required(redirect_field_name="login")
def pesquisar_cliente(request):
    comandas = Comandas.objects.filter(usuario_id=request.user.id).order_by("-id")
    busca = request.GET.get("pesquisar_cliente")
    clientes = Clientes.objects.filter().order_by("-id")

    if busca:
        clientes = Clientes.objects.filter(
            Q(nome__icontains=busca) | Q(cpf__icontains=busca)
        ).order_by("-id")

        for cliente in clientes:
            comanda = Comandas.objects.filter(cliente=cliente).first()
            if comanda:
                cliente.saldo = comanda.saldo
            else:
                cliente.saldo = 0.00
    else:
        clientes = []

    paginator = Paginator(clientes, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    alert_message = "Clique no nome do cliente para abrir a comanda."

    return render(
        request,
        "pages/pesquisar_cliente.html",
        {"clientes": page_obj, "comandas": comandas, "alert_message": alert_message},
    )


    # busca = request.GET.get("pesquisar_cliente")
    # clientes = Clientes.objects.filter().order_by("-id")

    # if busca:
    #     clientes = Clientes.objects.filter(
    #         Q(nome__icontains=busca) | Q(cpf__icontains=busca)
    #     )

    # paginator = Paginator(clientes, 5)  # Exibe 5 registros por página
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)

    # return render(request, "pages/pesquisar_cliente.html", {"clientes": page_obj})

    # busca = request.GET.get("pesquisar_cliente")
    # clientes = Clientes.objects.filter().order_by("-id")

    # if busca:
    #     clientes = Clientes.objects.filter(
    #         Q(nome__icontains=busca) | Q(cpf__icontains=busca)
    #     )

    # paginator = Paginator(clientes, 5)  # Exibe 5 registros por página
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)

    # return render(request, "pages/pesquisar_cliente.html", {"clientes": page_obj})
def redirecionar_recarregar_comanda(request, id):
    return redirect("recarregar_comanda", id=id)
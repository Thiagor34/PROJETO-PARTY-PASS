from django.contrib import admin
from .models import Clientes

class AdminContacts(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'cpf', 'telefone', 'data_nascimento', 'endereco']
    search_fields = ['nome']
    list_filter = ['nome', 'cpf']
    list_display_links = ['nome']

admin.site.register(Clientes, AdminContacts)
from django.contrib import admin
from .models import Produtos

# Register your models here.

class AdminProdutos(admin.ModelAdmin):
    list_display = ['id', 'nome', 'valor', 'categoria', 'descricao']
    search_fields = ['nome']
    list_filter = ['nome']
    list_display_links = ['nome']
    
    
admin.site.register(Produtos, AdminProdutos)
from django.contrib import admin
from .models import Comandas


class AdminComandas(admin.ModelAdmin):
    list_display = ['id', 'saldo']
    search_fields = ['saldo']
    list_filter = ['saldo']
    list_display_links = ['saldo']


admin.site.register(Comandas, AdminComandas)

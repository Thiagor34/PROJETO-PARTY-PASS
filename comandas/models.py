from distutils.command.upload import upload
from pyexpat import model
from clientes.models import Clientes
from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Comandas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=6, decimal_places=2)
    ultima_recarga = models.DateField(default=date.today)
    forma_pagamento = models.CharField(max_length=20)

    def __str__(self):
        return str(self.saldo)

    class Meta:
        verbose_name_plural = 'Comandas'
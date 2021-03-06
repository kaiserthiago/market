import datetime

import os

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from market.settings import BASE_DIR


class Cliente(models.Model):
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255, null=True)
    inscricao_estadual = models.CharField(max_length=20)
    inscricao_municipal = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    fone = models.CharField(max_length=13)
    logo = models.ImageField

    class Meta:
        ordering = ['nome_fantasia', 'razao_social']

    def __str__(self):
        return self.nome_fantasia


class Categoria(models.Model):
    descricao = models.CharField(max_length=150)

    class Meta:
        ordering = ['descricao']

    def __str__(self):
        return self.descricao


class Marca(models.Model):
    descricao_marca = models.CharField(max_length=150)

    class Meta:
        ordering = ['descricao_marca']

    def __str__(self):
        return self.descricao_marca


class UnidadeMedida(models.Model):
    descricao = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Unidades de medida'
        ordering = ['descricao']

    def __str__(self):
        return self.descricao


class Produto(models.Model):
    descricao = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria)
    marca = models.ForeignKey(Marca, null=True)
    imagem = models.ImageField(null=True, blank=True, upload_to='img_produtos')
    unidade_de_medida = models.ForeignKey(UnidadeMedida)

    class Meta:
        ordering = ['descricao']

    def __str__(self):
        return self.descricao


class Promocao(models.Model):
    cliente = models.ForeignKey(Cliente)
    produto = models.ForeignKey(Produto)
    data_inicio = models.DateField(default=datetime.date.today)
    data_fim = models.DateField()
    valor = models.DecimalField(decimal_places=2, max_digits=5)

    class Meta:
        verbose_name_plural = 'Promoções'
        ordering = ['produto', 'valor']


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    cliente = models.OneToOneField(Cliente, unique=True, blank=True, null=True)
    cpf = models.CharField(max_length=35, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    numero = models.CharField(max_length=20, null=True, blank=True)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    bairro = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=15, null=True, blank=True)
    pais = models.CharField(max_length=15, null=True, blank=True)
    cep = models.CharField(max_length=15, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)

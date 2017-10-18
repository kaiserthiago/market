from django.db.models import Avg, Count
from datetime import date
from django.shortcuts import render, redirect

# função pra trazer post pela categoria clicada
from supermarket.forms import FormPromocao, FormProduto
from supermarket.models import Produto, Categoria, Cliente, Marca, Promocao


def produtos_por_categoria(request, categoria_id):
    todas_categorias = Categoria.objects.all()
    categoria = Categoria.objects.filter(pk=categoria_id)
    filtro_produtos = Promocao.objects.filter(produto__categoria_id=categoria)

    context = {
        'todos_produtos': filtro_produtos,
        'todas_categorias': todas_categorias,
        'categoria': categoria,
    }

    return render(request, 'supermarket/produtos.html', context)


def promocao_por_produto(request, produto_id):
    todas_categorias = Categoria.objects.all()
    filtro_produtos = Promocao.objects.filter(produto=produto_id, data_fim__gte=date.today()).order_by(
        'valor', 'data_fim', 'produto__descricao', 'cliente__nome_fantasia')
    descricao = Produto.objects.filter(id=produto_id)

    context = {
        'todos_produtos': filtro_produtos,
        'todas_categorias': todas_categorias,
        'produto_descricao': descricao,
    }

    return render(request, 'supermarket/promocoes_por_produto.html', context)

# def order_promocao_por_produto(request, ordem, produto_id):
#     todas_categorias = Categoria.objects.all()
#     filtro_produtos = Promocao.objects.filter(produto=produto_id, data_fim__gte=date.today()).order_by(
#         'valor', 'data_fim', 'produto__descricao', 'cliente__nome_fantasia')
#     descricao = Produto.objects.filter(id=produto_id)
#
#     context = {
#         'todos_produtos': filtro_produtos,
#         'todas_categorias': todas_categorias,
#         'produto_descricao': descricao,
#     }
#
#     return render(request, 'supermarket/promocoes_por_produto.html', context)


def teste2(request):
    return render(request, 'supermarket/teste2.html', {})

def base(request):
    return render(request, 'supermarket/base.html', {})

def home(request):
    return render(request, 'supermarket/home.html', {})


def sobre(request):
    return render(request, 'supermarket/sobre.html', {})


def contato(request):
    return render(request, 'supermarket/contato.html', {})


def produtos(request):
    todos_produtos = Produto.objects.all()
    todas_categorias = Categoria.objects.all()

    context = {
        'todos_produtos': todos_produtos,
        'todas_categorias': todas_categorias,
    }

    return render(request, 'supermarket/produtos.html', context)


def promocoes(request):
    todas_categorias = Categoria.objects.all()
    todos_produtos = Promocao.objects.filter(data_fim__gte=date.today()).order_by(
        'data_fim', 'produto__descricao', 'cliente__nome_fantasia')
    clientes = Cliente.objects.all()

    context = {
        'todas_categorias': todas_categorias,
        'todos_produtos': todos_produtos,
        'clientes': clientes,
    }

    return render(request, 'supermarket/promocoes.html', context)


def filtro_promocoes(request, cliente_id):
    todas_categorias = Categoria.objects.all()
    todos_produtos = Promocao.objects.filter(cliente=cliente_id, data_fim__gte=date.today()).order_by(
        'data_fim', 'produto__descricao', 'cliente__nome_fantasia')
    clientes = Cliente.objects.all()

    context = {
        'todas_categorias': todas_categorias,
        'todos_produtos': todos_produtos,
        'clientes': clientes,
    }

    return render(request, 'supermarket/promocoes.html', context)

def nova_promocao(request):
    form = FormPromocao(request.POST)

    if form.is_valid():

        promocao = Promocao()

        promocao.cliente = form.cleaned_data['cliente']
        promocao.produto = form.cleaned_data['produto']
        promocao.data_inicio = form.cleaned_data['data_inicio']
        promocao.data_fim = form.cleaned_data['data_fim']
        promocao.valor = form.cleaned_data['valor']
        promocao.save()

        return redirect('supermarket.home')
    else:

        form = FormPromocao()

    return render(request, 'supermarket/novo_promocao.html', {'nova_promocao': form})


def novo_produto(request):
    form = FormProduto(request.POST)

    if form.is_valid():

        produto = Produto()

        produto.categoria = form.cleaned_data['categoria']
        produto.descricao = form.cleaned_data['descricao']
        produto.marca = form.cleaned_data['marca']
        produto.unidade_de_medida = form.cleaned_data['unidade_de_medida']
        produto.imagem = form.cleaned_data['imagem']
        produto.save()

        return redirect('supermarket.home')
    else:

        form = FormProduto()

    return render(request, 'supermarket/novo_produto.html', {'novo_produto': form})

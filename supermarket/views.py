from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Avg, Count, Min
from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
import json
import datetime

# função pra trazer post pela categoria clicada
from supermarket.forms import PromocaoForm, FormProduto, UserForm, UserProfileForm
from supermarket.models import Produto, Categoria, Cliente, Marca, Promocao, UserProfile


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


def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError


def promocao_por_produto(request, produto_id):
    todas_categorias = Categoria.objects.all()
    filtro_produtos = Promocao.objects.filter(produto=produto_id, data_fim__gte=date.today()).order_by(
        'valor', 'data_fim', 'produto__descricao', 'cliente__nome_fantasia')
    descricao = Produto.objects.filter(id=produto_id)

    # cont = Promocao.objects.filter(produto=produto_id).count()
    #
    # for cliente in cont:
    #     teste = Promocao.objects.filter(produto=produto_id, cliente=cliente.id).order_by('data_inicio')

    queryset = Promocao.objects.filter(produto=produto_id).annotate(min_valor=Min('valor')).order_by('data_inicio')
    datas = [obj.data_inicio for obj in queryset]
    precos = [float(obj.min_valor) for obj in queryset]

    context = {
        'todos_produtos': filtro_produtos,
        'todas_categorias': todas_categorias,
        'produto_descricao': descricao,
        'datas': json.dumps(datas, default=date_handler),
        'precos': json.dumps(precos),
    }

    return render(request, 'supermarket/promocoes_por_produto.html', context)


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
    todas_categorias = Promocao.objects.filter(data_fim__gte=date.today()).order_by(
        'produto__categoria__descricao').values('produto__categoria', 'produto__categoria__descricao').distinct()
    todos_produtos = Promocao.objects.filter(data_fim__gte=date.today()).order_by(
        'data_fim', 'produto__descricao', 'valor', 'cliente__nome_fantasia')
    clientes = Cliente.objects.all()

    # page = request.GET.get('page', 1)
    # paginator = Paginator(produtos, 4)
    #
    # try:
    #     todos_produtos = paginator.page(page)
    # except PageNotAnInteger:
    #     todos_produtos = paginator.page(1)
    # except EmptyPage:
    #     todos_produtos = paginator.page(paginator.num_pages)

    context = {
        'todas_categorias': todas_categorias,
        'todos_produtos': todos_produtos,
        'clientes': clientes,
    }

    return render(request, 'supermarket/promocoes.html', context)


def filtro_promocoes(request, cliente_id):
    todas_categorias = Categoria.objects.all()
    todos_produtos = Promocao.objects.filter(cliente=cliente_id, data_fim__gte=date.today()).order_by(
        'data_fim', 'produto__descricao', 'valor', 'cliente__nome_fantasia')
    clientes = Cliente.objects.all()

    context = {
        'todas_categorias': todas_categorias,
        'todos_produtos': todos_produtos,
        'clientes': clientes,
    }

    return render(request, 'supermarket/promocoes.html', context)


@login_required
def nova_promocao(request):
    if request.method == 'POST':
        form = PromocaoForm(request.POST)
        if form.is_valid():
            promocao = Promocao()

            promocao.cliente = request.user.userprofile.cliente
            promocao.produto = form.cleaned_data['produto']
            promocao.data_inicio = form.cleaned_data['data_inicio']
            promocao.data_fim = form.cleaned_data['data_fim']
            promocao.valor = form.cleaned_data['valor']
            promocao.save()

            return redirect('supermarket.home')

    form = PromocaoForm()

    context = {
        'form': form,
    }
    return render(request, 'supermarket/novo_promocao.html', context)


@login_required
def minhas_promocoes(request):
    promocoes = Promocao.objects.filter(cliente=request.user.userprofile.cliente).order_by('-data_fim')
    cliente = get_object_or_404(Cliente, pk=request.user.userprofile.cliente.id)

    context = {
        'promocoes': promocoes,
        'cliente': cliente,
    }
    return render(request, 'supermarket/minhas_promocoes.html', context)


@login_required
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


@login_required
def meus_dados(request):
    user = User.objects.get(pk=request.user.pk)
    user_form = UserForm(instance=user)

    try:
        user_profile = UserProfile.objects.get(user=user)
    except:
        user_profile = UserProfile()
        user_profile.user = user
        user_profile.save()

    profile_form = UserProfileForm(instance=user_profile)

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user.first_name = user_form.cleaned_data['first_name']
            user.last_name = user_form.cleaned_data['last_name']
            user.save()

            user_profile.cpf = profile_form.cleaned_data['cpf']
            user_profile.endereco = profile_form.cleaned_data['endereco']
            user_profile.numero = profile_form.cleaned_data['numero']
            user_profile.complemento = profile_form.cleaned_data['complemento']
            user_profile.cidade = profile_form.cleaned_data['cidade']
            user_profile.bairro = profile_form.cleaned_data['bairro']
            user_profile.estado = profile_form.cleaned_data['estado']
            user_profile.pais = profile_form.cleaned_data['pais']
            user_profile.cep = profile_form.cleaned_data['cep']
            user_profile.telefone = profile_form.cleaned_data['telefone']
            user_profile.save()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'user': user,
    }

    return render(request, 'supermarket/meus_dados.html', context)

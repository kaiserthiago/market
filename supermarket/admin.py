from supermarket.models import Cliente, Categoria, Marca, UnidadeMedida, Produto, Promocao
from django.contrib import admin

# Register your models here.

#classe para ordenar a exibição, criando colunas
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome_fantasia', 'razao_social')
    search_fields = ['nome_fantasia', 'razao_social']

#classe para ordenar a exibição, criando colunas
class MarcaAdmin(admin.ModelAdmin):
    search_fields = ['descricao_marca']

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'categoria')
    search_fields = ['descricao', 'categoria']

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['descricao']

class PromocaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'produto', 'data_inicio', 'data_fim', 'valor')
    search_fields = ['cliente', 'produto', 'cliente']
    list_filter = ['cliente', 'produto', 'data_inicio', 'data_fim', 'valor']

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(UnidadeMedida)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Promocao, PromocaoAdmin)
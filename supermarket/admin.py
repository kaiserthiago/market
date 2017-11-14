from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from supermarket.models import Cliente, Categoria, Marca, UnidadeMedida, Produto, Promocao, UserProfile
from django.contrib import admin


# Register your models here.

# classe para ordenar a exibição, criando colunas
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome_fantasia', 'razao_social')
    search_fields = ['nome_fantasia', 'razao_social']


# classe para ordenar a exibição, criando colunas
class MarcaAdmin(admin.ModelAdmin):
    search_fields = ['descricao_marca']


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'id', 'categoria')
    search_fields = ['descricao', 'categoria']


class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['descricao']


class PromocaoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'produto', 'data_inicio', 'data_fim', 'valor', 'id')
    list_filter = ['cliente', 'produto', 'data_inicio', 'data_fim', 'valor']


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(UnidadeMedida)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Promocao, PromocaoAdmin)

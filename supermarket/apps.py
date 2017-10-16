from __future__ import unicode_literals
import algoliasearch_django as algoliasearch
from algoliasearch_django import AlgoliaIndex
from django.apps import AppConfig

class SupermarketConfig(AppConfig):
    name = 'supermarket'

    def ready(self):
        Produto = self.get_model('Produto')
        Promocao = self.get_model('Promocao')
        algoliasearch.register(Produto, ProdutoIndex)
        algoliasearch.register(Promocao, PromocaoIndex)

class ProdutoIndex(AlgoliaIndex):
    fields = ('id', 'descricao', 'marca', 'unidade_de_medida', 'imagem')
    settings = {'searchableAttributes': ['descricao', 'marca', 'unidade_de_medida', 'id'],
                'customRanking': ['asc(descricao)'],}
    index_name = 'lista_produto'


class PromocaoIndex(AlgoliaIndex):
    fields = ('id', 'produto', 'cliente')
    settings = {'searchableAttributes': ['produto', 'cliente']}
    index_name = 'promocao'
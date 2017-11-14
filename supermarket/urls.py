#imports
from django.conf.urls import url
from django.conf.urls.static import static

from market import settings
from supermarket import views

urlpatterns=[
    url(r'^$', views.home, name='supermarket.home'),
    url(r'^produto$', views.produtos, name='supermarket.produtos'),
    url(r'^produto/novo$', views.novo_produto, name='supermarket.novo_produto'),
    url(r'^produto/(?P<categoria_id>[\d]+)', views.produtos_por_categoria, name='supermarket.produtos_por_categoria'),
    url(r'^promocao$', views.promocoes, name='supermarket.promocoes'),
    url(r'^promocao/(?P<cliente_id>[\d]+)', views.filtro_promocoes, name='supermarket.filtro_promocao'),
    url(r'^promocao/novo$', views.nova_promocao, name='supermarket.nova_promocao'),
    url(r'^promocao_por_produto/(?P<produto_id>[\d]+)', views.promocao_por_produto, name='supermarket.promocao_por_produto'),
    # url(r'^promocao_por_produto/order/(?P<ordem>[\d]+/(?P<produto_id>[\d]+)', views.order_promocao_por_produto, name='supermarket.order_promocao_por_produto'),
    url(r'^sobre$', views.sobre, name='supermarket.sobre'),
    url(r'^contato$', views.contato, name='supermarket.contato'),
    url(r'^meus_dados', views.meus_dados, name='supermarket.meus_dados'),

]

from django import forms
from django.contrib.auth.models import User
from bootstrap_datepicker.widgets import DatePicker

from supermarket.models import Promocao, Produto, UserProfile


class PromocaoForm(forms.ModelForm):
    valor = forms.DecimalField(min_value=0,
                               max_digits=32,
                               decimal_places=2,
                               initial="0",
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control input-sm required'}))

    class Meta:
        model = Promocao
        fields = ['produto', 'data_inicio', 'data_fim', 'valor']

        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'data_inicio': forms.TextInput(attrs={'class': 'form-control', 'id': 'data_inicio'}),
            'data_fim': forms.TextInput(attrs={'class': 'form-control', 'id': 'data_fim'}),

        }

        labels = {
            'produto': "Produto",
            'data_inicio': "Início",
            'data_fim': "Fim",
            'valor': "Preço",
        }


class FormProduto(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormProduto, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Produto
        fields = ['categoria', 'descricao', 'marca', 'unidade_de_medida', 'imagem']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'first_name': "Nome",
            'last_name': "Sobrenome",
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'cliente', 'remote_customer_id')

        widgets = {
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'cpf': "CPF",
            'endereco': "Endereço",
            'numero': "Número",
            'complemento': "Complemento",
            'cidade': "Cidade",
            'bairro': "Bairro",
            'estado': "Estado",
            'pais': "País",
            'cep': "CEP",
            'telefone': "Telefone",
        }

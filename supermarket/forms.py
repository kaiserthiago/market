from django import forms
from django.contrib.auth.models import User

from supermarket.models import Promocao, Produto, UserProfile


class FormPromocao(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormPromocao, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Promocao
        fields = ['cliente', 'produto', 'data_inicio', 'data_fim', 'valor']


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
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'first_name': "Nome",
            'last_name': "Sobrenome",
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'remote_customer_id')

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

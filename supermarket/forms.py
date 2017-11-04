from django.forms import ModelForm
from supermarket.models import Promocao, Produto


class FormPromocao(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormPromocao, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Promocao
        fields = ['cliente', 'produto', 'data_inicio', 'data_fim', 'valor']


class FormProduto(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormProduto, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Produto
        fields = ['categoria', 'descricao', 'marca', 'unidade_de_medida', 'imagem']

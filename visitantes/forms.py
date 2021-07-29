from django import forms
from visitantes.models import Visitante


class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = [
            "nome_completo",
            "cpf",
            "data_nascimento",
            "numero_casa",
            "placa_veiculo",
        ]
        error_messages = {
            "nome_completo": {"required": "O nome completo do visitante é obrigatório"},
            "cpf": {"required": "O cpf do visitante é obrigatório"},
            "data_nascimento": {
                "required": "A data do visitante é obrigatória",
                "invalid": "Adicione uma data válida (DD/MM/AAAA)",
            },
        }


class AutorizaVisitanteForm(forms.ModelForm):
    morador_responsavel = forms.CharField(required=True)

    class Meta:
        model = Visitante
        fields = ["morador_responsavel"]
        error_messages = {
            "morador_responsavel": {
                "required": "Porfavor, informe o nome do morador responsável pela entrada do visitante"
            }
        }

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

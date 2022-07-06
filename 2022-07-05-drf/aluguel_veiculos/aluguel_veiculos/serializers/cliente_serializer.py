from rest_framework import serializers
from aluguel_veiculos.models.cliente import Cliente
import re

from aluguel_veiculos.validator.cpf_validator import valida_cpf


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    telefone = serializers.CharField(min_length=9)
    cnpj = serializers.CharField(required=False)
    cpf = serializers.CharField(required=False)

    class Meta():
        model = Cliente
        fields = "__all__"

    def validate(self, data):
        if (data.get("tipo") == 'PJ') and (data.get("cnpj") == None):
            raise serializers.ValidationError(
                {'Tipo': 'Se tipo igual a PJ o cnpj é obrigatorio'})
        elif (data.get("tipo") == 'PF') and (data.get("cpf") == None):
            raise serializers.ValidationError(
                'Se tipo igual a PF o cpf é obrigatorio')

        return data

    def validate_tipo(self, tipo):
        return tipo

    def validate_nome(self, nome):
        return nome

    def validate_cpf(self, cpf):
        if valida_cpf(cpf):
            raise serializers.ValidationError(
                {'CPF': 'CPF deve ser numerico'})

        return cpf

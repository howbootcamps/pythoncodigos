from rest_framework import serializers
from aluguel_veiculos.models import Cliente, Veiculo


# Serializers define the API representation.
class ClienteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta():
        model = Cliente
        fields = ['url', 'nome', 'endereco', 'telefone', 'cpf', 'cnpj', 'tipo']


# Serializers define the API representation.
class VeiculoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta():
        model = Veiculo
        fields = ['url', 'placa', 'km', 'carga', 'bagageiro', 'portas', 'tipo']

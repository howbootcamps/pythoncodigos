from rest_framework import serializers
from aluguel_veiculos.models.aluguel import Aluguel


class ListaAlugueisClienteSerializer(serializers.ModelSerializer):
    veiculo = serializers.ReadOnlyField(source='veiculo.placa')
    cliente = serializers.ReadOnlyField(source='cliente.nome')

    class Meta:
        model = Aluguel
        fields = [
            'cliente',
            'veiculo',
            'data_retirada',
            'data_devolucao',
            'km_rodado',
            'valor',
        ]

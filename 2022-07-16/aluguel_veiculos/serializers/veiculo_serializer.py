from rest_framework import serializers
from aluguel_veiculos.models.veiculo import Veiculo


class VeiculoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta():
        model = Veiculo
        fields = "__all__"

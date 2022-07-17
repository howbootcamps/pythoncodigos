from email.policy import default
from rest_framework import serializers
from aluguel_veiculos.models.aluguel import Aluguel


class AluguelSerializer(serializers.HyperlinkedModelSerializer):    
    km_rodado = serializers.FloatField()
    data_retirada = serializers.DateField(read_only=True)
    data_devolucao = serializers.DateField(read_only=True)    
    valor = serializers.FloatField(required=False, read_only=True)

    def create(self, validated_data):
        
        validated_data['valor'] = validated_data['km_rodado'] * 1.5
        return super().create(validated_data)        

    class Meta():
        model = Aluguel
        fields = "__all__"

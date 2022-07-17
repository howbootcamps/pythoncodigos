from rest_framework import viewsets
from rest_framework import permissions
from aluguel_veiculos.models.veiculo import Veiculo
from aluguel_veiculos.serializers.veiculo_serializer import VeiculoSerializer


class VeiculoViewset(viewsets.ModelViewSet):
    serializer_class = VeiculoSerializer
    queryset = Veiculo.objects.all()
    permission_classes = [permissions.IsAuthenticated]

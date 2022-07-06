from rest_framework import viewsets

from aluguel_veiculos.models import Cliente, Veiculo
from aluguel_veiculos.serializer import ClienteSerializer, VeiculoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
from rest_framework import viewsets
from rest_framework import permissions
from aluguel_veiculos.models.cliente import Cliente
from aluguel_veiculos.serializers.cliente_serializer import ClienteSerializer


class ClienteViewset(viewsets.ModelViewSet):

    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    permission_classes = [permissions.IsAuthenticated]

from rest_framework import viewsets, filters
from rest_framework import permissions
from aluguel_veiculos.models.cliente import Cliente
from aluguel_veiculos.serializers.cliente_serializer import ClienteSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ClienteViewset(viewsets.ModelViewSet):

    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    search_fields = ['nome', 'endereco']
    ordering_fields = ['nome']

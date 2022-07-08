from rest_framework.response import Response
from rest_framework import viewsets
from locadora.models.cliente import Cliente
from locadora.serializers.cliente_serializer import ClienteSerializer


class ClienteViewset(viewsets.ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

from rest_framework import viewsets
from rest_framework import permissions
from aluguel_veiculos.models.aluguel import Aluguel
from aluguel_veiculos.serializers.aluguel_serializer import AluguelSerializer


class AluguelViewset(viewsets.ModelViewSet):

    serializer_class = AluguelSerializer
    queryset = Aluguel.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):        
        return super().create(request, *args, **kwargs)

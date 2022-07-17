from rest_framework import generics
from aluguel_veiculos.models.aluguel import Aluguel
from aluguel_veiculos.serializers.lista_alugueis_cliente_serializer import ListaAlugueisClienteSerializer


class ListaClientesVeiculoViewset(generics.ListAPIView):

    def get_queryset(self):
        queryset = Aluguel.objects.filter(veiculo_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaAlugueisClienteSerializer

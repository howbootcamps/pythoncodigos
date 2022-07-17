from django.urls import include, path
from rest_framework import routers
from aluguel_veiculos.views.aluguel_viewset import AluguelViewset
from aluguel_veiculos.views.cliente_viewset import ClienteViewset
from aluguel_veiculos.views.lista_alugueis_cliente_viewset import ListaAlugueisClienteViewset
from aluguel_veiculos.views.lista_clientes_veiculo_viewset import ListaClientesVeiculoViewset
from aluguel_veiculos.views.veiculo_viewset import VeiculoViewset

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewset)
router.register(r'veiculos', VeiculoViewset)
router.register(r'alugueis', AluguelViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('clientes/<int:pk>/alugueis/', ListaAlugueisClienteViewset.as_view()),
    path('veiculos/<int:pk>/alugueis/', ListaClientesVeiculoViewset.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

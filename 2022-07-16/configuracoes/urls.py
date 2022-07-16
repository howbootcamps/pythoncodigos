from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('v1/', include('aluguel_veiculos.urls')),
]

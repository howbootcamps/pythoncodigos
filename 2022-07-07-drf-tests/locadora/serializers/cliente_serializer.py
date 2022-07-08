from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from locadora.models.cliente import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(min_length=10,  max_length=120)

    class Meta:
        model = Cliente
        fields = "__all__"

from rest_framework import serializers
from .models import Tatuador, Cliente, Tatuagem

class TatuadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tatuador
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class TatuagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tatuagem
        fields = '__all__'

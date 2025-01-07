from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Tatuador, Cliente, Tatuagem
from .serializers import TatuadorSerializer, ClienteSerializer, TatuagemSerializer



class TatuadorViewSet(viewsets.ModelViewSet):
    queryset = Tatuador.objects.all()
    serializer_class = TatuadorSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class TatuagemViewSet(viewsets.ModelViewSet):
    queryset = Tatuagem.objects.all()
    serializer_class = TatuagemSerializer
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets , permissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Client , Stok_Type, Product_Type, Condominium,Client_Address
from .models import Product, Stok, Item, Stok_Moviment

from .serializer import ClientSerializer, Stok_TypeSerializer, Product_TypeSerializer
from .serializer import CondominiumSerializer, Client_AddressSerializer, ProductSerializer
from .serializer import StokSerializer, ItemSerializer, Stok_MovimentSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['name','doc']

class Stok_TypeViewSet(viewsets.ModelViewSet):
    queryset = Stok_Type.objects.all()
    serializer_class = Stok_TypeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['name']

class Product_TypeViewSet(viewsets.ModelViewSet):
    queryset = Product_Type.objects.all()
    serializer_class = Product_TypeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['name']

class CondominiumViewSet(viewsets.ModelViewSet):
    queryset = Condominium.objects.all()
    serializer_class = CondominiumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['name','address','neighborhood','city']

class Client_AddressViewSet(viewsets.ModelViewSet):
    queryset = Client_Address.objects.all()
    serializer_class = Client_AddressSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['Client', 'Condominium']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['name','Product_Type']

class StokViewSet(viewsets.ModelViewSet):
    queryset = Stok.objects.all()
    serializer_class = StokSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['name','Stok_Type']

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['sn', 'Product','Stok','User']

class Stok_MovimentViewSet(viewsets.ModelViewSet):
    queryset = Stok_Moviment.objects.all()
    serializer_class = Stok_MovimentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['Item', 'Stok', 'User']

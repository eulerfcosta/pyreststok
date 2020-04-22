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


class ClientViewSet(views.ModelViewSet):
    queryset = Client.object.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['name','doc']

class Stok_TypeViewSet(views.ModelViewSet):
    queryset = Stok_Type.object.all()
    serializer_class = Stok_TypeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['name']

class Product_TypeViewSet(views.ModelViewSet):
    queryset = Product_Type.object.all()
    serializer_class = Product_TypeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['name']

class CondominiumViewSet(views.ModelViewSet):
    queryset = Condominium.object.all()
    serializer_class = CondominiumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['name','address','neighborhood','city']

class Client_AddressViewSet(views.ModelViewSet):
    queryset = Client_Address.object.all()
    serializer_class = Client_AddressSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['Client', 'Condominium']

class ProductViewSet(views.ModelViewSet):
    queryset = Product.object.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['name','Product_Type']

class StokViewSet(views.ModelViewSet):
    queryset = Stok.object.all()
    serializer_class = StokSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['name','Stok_Type']

class ItemViewSet(views.ModelViewSet):
    queryset = Item.object.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['sn', 'Product','Stok','User']

class Stok_MovimentViewSet(views.ModelViewSet):
    queryset = Client.object.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['Item', 'Stok', 'User']

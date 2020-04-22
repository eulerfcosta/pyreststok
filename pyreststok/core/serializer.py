from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Client , Stok_Type, Product_Type, Condominium,Client_Address
from .models import Product, Stok, Item, Stok_Moviment

from .filters import ClientFilter, Stok_TypeFilter, Product_TypeFilter
from .filters import CondominiumFilter, Client_AddressFilter, ProductFilter
from .filters import StokFilter, ItemFilter, Stok_MovimentFilter



class ClientSerializer(serializer.ModelSerializer):
    filterset_class = ClientFilter
    class Meta:
        model = Client
        exclude = []

class Stok_TypeSerializer(serializer.ModelSerializer):
    filterset_class = Stok_TypeFilter
    class Meta:
        model = Stok_Type
        exclude = []

class Product_TypeSerializer(serializer.ModelSerializer):
    filterset_class = Product_TypeFilter
    class Meta:
        model = Product_Type
        exclude = []

class CondominiumSerializer(serializer.ModelSerializer):
    filterset_class = CondominiumFilter
    class Meta:
        model = Condominium
        exclude = []

class Client_AddressSerializer(serializer.ModelSerializer):
    filterset_class = Client_AddressFilter
    class Meta:
        model = Client_Address
        exclude = []

class ProductSerializer(serializer.ModelSerializer):
    filterset_class = ProductFilter
    class Meta:
        model = Product
        exclude = []

class StokSerializer(serializer.ModelSerializer):
    filterset_class = StokFilter
    class Meta:
        model = Stok
        exclude = []

class ItemSerializer(serializer.ModelSerializer):
    filterset_class = ItemFilter
    class Meta:
        model = Item
        exclude = []

class Stok_MovimentSerializer(serializer.ModelSerializer):
    filterset_class = Stok_MovimentFilter
    class Meta:
        model = Stok_Moviment
        exclude = []

from django_filters import rest_framework as filters

from .models import Client , Stok_Type, Product_Type, Condominium,Client_Address
from .models import Product, Stok, Item, Stok_Moviment


class ClientFilter(filters.FilterSet):

    class Meta:
        model = Client
        fields = {
            'name' : ['icontains'],
            'doc' : ['icontains']
        }

class Stok_TypeFilter(filters.FilterSet):

    class Meta:
        model = Stok_Type
        fields = {
            'name' : ['icontains']
        }

class Product_TypeFilter(filters.FilterSet):

    class Meta:
        model = Product_Type
        fields = {
            'name' : ['icontains']
        }

class CondominiumFilter(filters.FilterSet):

    class Meta:
        model = Condominium
        fields = {
            'name' : ['icontains'],
            'address' : ['icontains'],
            'neighborhood' : ['icontains'],
            'city' : ['icontains']
        }

class Client_AddressFilter(filters.FilterSet):

    class Meta:
        model = Client_Address
        fields = {
            'Client',
            'Condominium'
        }

class ProductFilter(filters.FilterSet):

    class Meta:
        model = Product
        fields = {
            'name' : ['icontains'],
            'Product_Type'
        }

class StokFilter(filters.FilterSet):

    class Meta:
        model = Stok
        fields = {
            'name' : ['icontains'],
            'Stok_Type'
        }

class ItemFilter(filters.FilterSet):

    class Meta:
        model = Item
        fields = {
            'Product',
            'Stok',
            'User',
            'sn' : ['icontains']
        }

class Stok_MovimentFilter(filters.FilterSet):

    class Meta:
        model = Stok_Moviment
        fields = {
            'Item',
            'Stok',
            'User'
        }

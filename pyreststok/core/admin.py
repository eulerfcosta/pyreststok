from django.contrib import admin

from .models import Client , Stok_Type, Product_Type, Condominium,Client_Address
from .models import Product, Stok, Item, Stok_Moviment

# Register your models here.


admin.site.register(Client)
admin.site.register(Stok_Type)
admin.site.register(Product_Type)
admin.site.register(Condominium)
admin.site.register(Client_Address)
admin.site.register(Product)
admin.site.register(Item)
admin.site.register(Stok)
admin.site.register(Stok_Moviment)

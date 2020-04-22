from django.urls import path
from rest_framework import routers

from .views import ClientViewSet, Stok_TypeViewSet,  Product_TypeViewSet
from .views import CondominiumViewSet, Client_AddressViewSet, ProductViewSet
from .views import StokViewSet, ItemViewSet, Stok_MovimentViewSet


router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'stokstypes', Stok_TypeViewSet)
router.register(r'productstypes', Product_TypeViewSet)
router.register(r'condominiums', CondominiumViewSet)
router.register(r'clientsaddresses', Client_AddressViewSet)
router.register(r'products', ProductViewSet)
router.register(r'stoks', StokViewSet)
router.register(r'items', ItemViewSet)
router.register(r'stokmoviments', Stok_MovimentViewSet)

core_urls = router.urls

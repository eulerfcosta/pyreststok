from django.urls import path
from rest_framework import routers

from .views import ClientViewSet , Stok_TypeViewSet, Product_TypeViewSet
from .views import CondominiumViewSet, Client_AddressViewSet, ProductViewSet
from .views import StokViewSet, ItemViewSet, Stok_MovimentViewSet


router = routers.DefaultRouter()
router.register(r'pyreststok/clients', ClientViewSet)
router.register(r'pyreststok/stokstypes', Stok_TypeViewSet)
router.register(r'pyreststok/productstypes', Product_TypeViewSet)
router.register(r'pyreststok/condominiums', CondominiumViewSet)
router.register(r'pyreststok/clientsaddresses', Client_AddressViewSet)
router.register(r'pyreststok/products', ProductViewSet)
router.register(r'pyreststok/stoks', StokViewSet)
router.register(r'pyreststok/items', ItemViewSet)
router.register(r'pyreststok/stokmoviments', Stok_MovimentViewSet)

core_urls = router.urls

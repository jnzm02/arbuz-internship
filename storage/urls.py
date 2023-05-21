from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ProductViewSet,
    CartViewSet,
    StorageViewSet,
)

router = DefaultRouter()

router.register('products', ProductViewSet)
router.register('carts', CartViewSet)
router.register('storages', StorageViewSet)

app_name = 'storage'

urlpatterns = [
    path('', include(router.urls)),
]

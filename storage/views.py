from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)

from rest_framework import (
    viewsets,
)

from .serializers import (
    ProductSerializer,
    CartCardSerializer,
    CartSerializer,
    StorageCardSerializer,
    StorageSerializer
)
from .models import (Product, CartCard, Cart, StorageCard, Storage)


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []


class ProductViewSet(BaseViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CartViewSet(BaseViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


class StorageViewSet(BaseViewSet):
    serializer_class = StorageSerializer
    queryset = Storage.objects.all()
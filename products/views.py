from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .serializers import ProductSerializers, BuyProductSerializer
from .models import BuyProduct, Product
from rest_framework.permissions import IsAuthenticated
from .authenticated import IsOwnerOrReadOnly


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()


class ProductCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, ]


class BuyProductListAPIView(ListAPIView):
    queryset = BuyProduct.objects.all()
    serializer_class = BuyProductSerializer


class ProductUpdateAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializers



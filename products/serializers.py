from rest_framework import serializers
from .models import *


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'author', 'firm', 'image', 'viloyat',
                  'tuman', 'cost', 'coifsenti', 'about', 'get_product']


class BuyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyProduct
        fields = ['author', 'product', 'count']

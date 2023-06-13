from rest_framework import serializers

from .models import products

class productsSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = products
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]
    def get_my_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            return None
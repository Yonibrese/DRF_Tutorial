from rest_framework import generics

from .models import products
from .serializers import productsSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = products.objects.all()
    serializer_class = productsSerializer
    # lookup_field = 'pk'

from rest_framework import generics

from .models import products
from .serializers import productsSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = products.objects.all()
    serializer_class = productsSerializer

    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        # print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")or None
        if content is None:
            content = title
        price = serializer.validated_data.get("price")
        serializer.save(content=content)

product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = products.objects.all()
    serializer_class = productsSerializer
    # lookup_field = 'pk'

product_detail_view = ProductDetailAPIView.as_view()


class ProductListApiView(generics.ListAPIView):
    '''
    This function is not in use
    '''
    queryset = products.objects.all()
    serializer_class = productsSerializer

product_list_view = ProductListApiView.as_view()
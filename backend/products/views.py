from rest_framework import generics

from .models import products
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
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


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = products.objects.all()
    serializer_class = productsSerializer
    # lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = products.objects.all()
    serializer_class = productsSerializer

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    


class ProductListApiView(generics.ListAPIView):
    '''
    This function is not in use
    '''
    queryset = products.objects.all()
    serializer_class = productsSerializer

product_list_view = ProductListApiView.as_view()


# single view for listAll(), GET(<id>), and POST
@api_view(["GET", "POST"])
def product_alt_view(request,pk=None ,*args, **kwargs):
    method = request.method 

    if method == "GET":
        # url perams
        if pk is not None:
            #detail view (get(ID))
            obj = get_object_or_404(products, pk=pk)
            data = productsSerializer(obj, many=False).data
            return Response(data)

        # list view (getALL)
        # get item based on url (no ID list all items)
        queryset = products.objects.all()
        data = productsSerializer(queryset, many=True).data
        return Response(data)

    if method == "POST":
        # create an Item
        serializer = productsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None
            if content is None:
                content = title
            serializer.save(content=content)

            return Response(serializer.data)
        return Response({"invalid":"not good data"}, status=400)


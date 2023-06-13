import json
# from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict
from products.models import products
from products.serializers import productsSerializer

@api_view(["POST"])
def api_home(request, *arg, **kwarg):
    serializer = productsSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        # data = serializer.save()
        return Response(serializer.data)
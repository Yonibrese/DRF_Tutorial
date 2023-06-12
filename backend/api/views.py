import json
# from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict
from products.models import products
from products.serializers import productsSerializer

@api_view(["GET","POST"])
def api_home(request, *arg, **kwarg):
    instance = products.objects.all().order_by("?").first()
    data = {}
    if instance:
      #  data = model_to_dict(instance, fields=['id','title','price', "sale_price"])
      data = productsSerializer(instance).data
    return Response(data)
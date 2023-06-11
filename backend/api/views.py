import json
from django.http import JsonResponse
from products.models import products

def api_home(request, *arg, **kwarg):
    model_data = products.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data["id"] = model_data.id
        data["title"] = model_data.title
        data["content"] = model_data.content
        data["price"] = model_data.price
    
    return JsonResponse(data)
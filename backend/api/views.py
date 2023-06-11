import json
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from products.models import products

def api_home(request, *arg, **kwarg):
    model_data = products.objects.all().order_by("?").first()
    data = {}
    if model_data:
       data = model_to_dict(model_data,fields=['id','title','price'])
    
    return JsonResponse(data)
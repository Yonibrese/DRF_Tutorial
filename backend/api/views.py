from django.http import JsonResponse

def api_home(request, *arg, **kwarg):
    return JsonResponse({"message":"Hello world from the DJANGO API"})
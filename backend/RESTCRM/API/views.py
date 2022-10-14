import json
from django.http import JsonResponse



def api_home(request, *args, **kwargs):
    body = request.body
    data= json.loads(body)
    print(data)
    return JsonResponse(data)
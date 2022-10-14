'''Module Responsible for API View'''
import json

from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    '''Func Takes in Request Sends Back Request Parameters'''
    body = request.body
    data= json.loads(body)
    print(data)
    return JsonResponse(data)

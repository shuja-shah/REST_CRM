'''Module Responsible for API View'''
import json

from django.http import JsonResponse
from Lists.models import List
from django.forms.models import model_to_dict


def api_home(request, *args, **kwargs):
    '''Func Takes in Request Sends Back Request Parameters'''
    model_data = List.objects.all().order_by('?').first()
    data= {}
    if model_data:
        data = model_to_dict(model_data)
    return JsonResponse(data)

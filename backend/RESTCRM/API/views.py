'''Module Responsible for API View'''
import json

from django.forms.models import model_to_dict
from Lists.models import List
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    '''Func Takes in Request Sends Back Request Parameters'''
    qurey= request.GET.get('id')
    model_data = List.objects.all().order_by('?').first()
    data= {}
    if model_data:
        data = model_to_dict(model_data)
        print(data)
    return Response(data)

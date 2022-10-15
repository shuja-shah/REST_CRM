'''Module Responsible for API View'''

from Lists.models import List
from Lists.serializers import ModelList
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    '''Func Retuns Data from DB'''
    model_instance = List.objects.all().order_by('?').first()
    data= {}
    if model_instance:
        data = ModelList(model_instance).data
    str('Not FOUND ERROR 404')
    return Response(data)

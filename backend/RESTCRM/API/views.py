'''Module Responsible for API View'''

from Lists.models import List
from Lists.serializers import ModelList
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    '''Func Retuns Data from DB'''
    if request.method == "GET":
        model_instance = List.objects.all().order_by('?').first()
        data= {}
        if model_instance:
            data = ModelList(model_instance).data
        str('Not FOUND ERROR 404')
        return Response(data)
    if request.method == "POST":
        serializer= ModelList(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
'''Module Responsible for API View'''

# from Lists.models import List
# from Lists.serializers import ModelList
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import List, user
from user.seralizer import User_SERIALIZATION


@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    '''Func Retuns Data from DB'''
    # if request.method == "GET":
    #     model_instance = List.objects.all().order_by('?').first()
    #     data= {}
    #     if model_instance:
    #         data = ModelList(model_instance).data
    #     str('Not FOUND ERROR 404')
    #     return Response(data)
    # if request.method == "POST":
    #     serializer= ModelList(data = request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)
    # Send request to create user!
    if request.method == 'POST':
        seralizer = User_SERIALIZATION(data = request.data)
        if seralizer.is_valid(raise_exception=True):
            seralizer.save()
            return Response('USER SUCCESFFULLY CREATED'), 201
        else:
            return Response('USER NOT CREATED'), 400
   
    if request.method == 'GET':
        # Get all tasks of that specific username
        username = request.GET.get('username')
        target = user.objects.get(username=username)
        if target:
            user_id= user.id
            tasks = List.objects.filter(user_id=user_id)
            return Response(tasks), 200
        else:
            return Response('No such user exists'), 400
            
        
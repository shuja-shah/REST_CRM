'''Module Responsible for API View'''

import json

from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import List, user
from user.seralizer import User_SERIALIZATION


@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    '''API Home'''
    if request.method == 'POST':
        seralizer = User_SERIALIZATION(data = request.data)
        if seralizer.is_valid(raise_exception=True):
            seralizer.save()
            return Response('USER SUCCESFFULLY CREATED'), 201
        else:
            return Response('USER NOT CREATED'), 400
   
    if request.method == 'GET':
        username = request.GET.get('username')
        target = user.objects.get_user(username=username)
        if target:
            target_id = target.id
            all_tasks = List.objects.filter(user=target_id)
            result = json.dumps([model_to_dict(task) for task in all_tasks])
            return Response(json.JSONDecoder().decode(result))
            
        else:
            return Response('No such user exists'), 400
            
        
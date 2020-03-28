from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import serializers
from . import models


@api_view(['POST'])
def registration_view(request):
    serializer = serializers.RegistrationSerializer(data=request.data)
    response = {}
    if serializer.is_valid():
        user = serializer.save()
        response['username'] = user.username
    else:
        response = serializer.errors
    return Response(response)

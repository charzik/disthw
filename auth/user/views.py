from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from . import serializers

@api_view(['POST'])
def registration_view(request):
    serializer = serializers.RegistrationSerializer(data=request.data)
    response = {}
    if serializer.is_valid():
        user = serializer.save()
        response['username'] = user.username
        response['token'] = Token.objects.get(user=user).key 
    else:
        response = serializer.errors
    return Response(response)
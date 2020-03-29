from requests import request as http_request

from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import serializers
from . import models


@api_view(['POST'])
def registration_view(request):
    confirm_url = 'some url'
    serializer = serializers.RegistrationSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors)

    user = serializer.save()
    notification_response = http_request(
        method=request.method,
        url='http://%s:%s/%s' % (
            settings.NOTIFICATION_HOST, 
            settings.NOTIFICATION_PORT, 
            'v1/send-registartion-email'
        ),
        json={
            'email': user.email,
            'confirm_url': confirm_url
        }
    )
    if not (notification_response.status_code == 200):
        return Response(status=500, data={'text': 'internal server error'})
    return Response(data={'username': user.username})

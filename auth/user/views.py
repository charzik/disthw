from requests import request as http_request
from datetime import datetime

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import (
    ObtainJSONWebToken,
    jwt_response_payload_handler,
)

from . import serializers
from . import models


@api_view(['POST'])
def registration_view(request):
    serializer = serializers.RegistrationSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(status=400, data=serializer.errors)

    user = serializer.save()
    try:
        notification_response = http_request(
            method='POST',
            url='http://%s:%s/%s'
            % (
                settings.NOTIFICATION_HOST,
                settings.NOTIFICATION_PORT,
                'v1/send-registartion-email',
            ),
            json={'email': user.email, 'confirm_url': user.confirm_url_id},
        )
    except:
        return Response(status=500, data={'text': 'internal server error'})
    if not (notification_response.status_code == 200):
        return Response(status=500, data={'text': 'internal server error'})
    return Response(data={'username': user.username})


class LoginView(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        serializer = super().get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            if not user.is_confirmed:
                return Response(
                    status=409, data={'text': 'Account did not confermed!'},
                )
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)
            response = Response(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (
                    datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
                )
                response.set_cookie(
                    api_settings.JWT_AUTH_COOKIE,
                    token,
                    expires=expiration,
                    httponly=True,
                )
            return response

        return Response(serializer.errors, status=400)


@api_view(['GET'])
def confirm_registration_view(request, url_id):
    try:
        account = models.Account.objects.get(confirm_url_id=url_id)
        if not account.is_confirmed:
            account.is_confirmed = True
            account.save()
        return Response(status=200, data={'text': 'Account confirmed!'})
    except ObjectDoesNotExist:
        return Response(status=404)

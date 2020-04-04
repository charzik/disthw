from requests import request as http_request
from datetime import datetime

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt import serializers as jwt_serializers
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.authentication import AUTH_HEADER_TYPES
from rest_framework import generics

from . import serializers
from . import models


@api_view(['POST'])
def registration_view(request):
    serializer = serializers.RegistrationSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(status=400, data=serializer.errors)

    user = serializer.save()
    confirm_url = 'http://%s:%s/v1/user/confirm/%s' % (
        settings.SERVICE_HOST,
        settings.SERVICE_PORT,
        user.confirm_url_id,
    )
    try:
        notification_response = http_request(
            method='POST',
            url='http://%s:%s/%s'
            % (
                settings.NOTIFICATION_HOST,
                settings.NOTIFICATION_PORT,
                'v1/send-registartion-email',
            ),
            json={'email': user.email, 'confirm_url': confirm_url},
        )
    except:
        return Response(status=500, data={'text': 'internal server error'})
    if not (notification_response.status_code == 200):
        return Response(status=500, data={'text': 'internal server error'})
    return Response(data={'username': user.username})


class LoginView(generics.GenericAPIView):
    permission_classes = ()
    authentication_classes = ()

    serializer_class = jwt_serializers.TokenObtainPairSerializer

    www_authenticate_realm = 'api'

    def get_authenticate_header(self, request):
        return '{0} realm="{1}"'.format(
            AUTH_HEADER_TYPES[0],
            self.www_authenticate_realm,
        )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            user = models.Account.objects.get(email=request.data['email'])
            if not user.is_confirmed:
                return Response(
                    status=409, data={'text': 'Account did not confermed!'},
                )
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=200)


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

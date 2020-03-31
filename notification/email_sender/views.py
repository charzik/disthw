from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings

from . import tasks


@api_view(['POST'])
def send_registration_email(request):
    if ('email' not in request.data) or ('confirm_url' not in request.data):
        return Response(
            status=400,
            data={'text': '(email, confirm_url) is required fields'},
        )

    tasks.send_registartion_email.delay(
        receiver_email=request.data['email'],
        confirm_url=request.data['confirm_url'],
        sender_email=settings.EMAIL_USER,
        sender_password=settings.EMAIL_PASSWORD,
    )
    return Response(status=200)

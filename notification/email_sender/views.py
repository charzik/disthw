from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import tasks

@api_view(['POST'])
def send_registration_email(request):
    if ('email' not in request.data) or ('confirm_url' not in request.data):
        return Response(
            status=400, 
            data={'text': '(email, confirm_url) is required fields'}
        )
    
    tasks.send_registartion_email.delay(
        email=request.data['email'], 
        confirm_url=request.data['confirm_url']
    )
    return Response(status=200)

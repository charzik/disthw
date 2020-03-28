from requests import request as proxy_request

from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def proxy_view(request, url):
    user = request.user
    headers = dict(request.headers)
    headers.update({
        'X-Username': user.username,
        'X-Email': user.email,
    })
    headers.pop('Authorization')
    try:
        response = proxy_request(
            method=request.method,
            url='http://%s:%s/%s' % (
                settings.PROXY_HOST, 
                settings.PROXY_PORT, 
                url
            ),
            params=request.query_params,
            headers=headers,
            json=request.data
        )
        return Response(
            data=response.json(),
            status=response.status_code, 
            content_type=response.headers['Content-Type'],
        )
    except:
        return Response(status=500, data={'text': 'Internal server error'})
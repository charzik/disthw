from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API')

urlpatterns = [
    path('docs', schema_view),
    path('v1/', include('items.urls'))
]

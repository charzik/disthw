from django.urls import path, include

urlpatterns = [
    path('v1/import-items', include('items_importer.urls')),
]

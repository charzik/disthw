from rest_framework import serializers

from . import models

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Item
        fields = ['price', 'name', 'category', 'id']
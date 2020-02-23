from rest_framework import serializers

from . import models

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Item
        fields = ['code', 'name', 'category']
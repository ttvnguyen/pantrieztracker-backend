from .models import ImageModel

from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our GallerySerializer
class GallerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = ImageModel
        # the fields that should be included in the serialized output
        fields = ['id', 'img']
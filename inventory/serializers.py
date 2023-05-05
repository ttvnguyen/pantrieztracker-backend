from .models import Inventory

from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our InventorySerializer
class InventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Inventory
        # the fields that should be included in the serialized output
        fields = ['id', 'qty', 'image','item', 'category', 'expiry']
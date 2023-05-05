from django.shortcuts import render
from .models import Inventory
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import InventorySerializer

# Create your views here.
class InventoryViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Inventory.objects.all()
    # The serializer class for serializing output
    serializer_class = InventorySerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Could be [permissions.IsAuthenticated]

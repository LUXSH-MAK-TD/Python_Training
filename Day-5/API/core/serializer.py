# This file was previously named 'serializer .py' with a space.
# Renamed to 'serializer.py' for proper Python import conventions.

from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description']

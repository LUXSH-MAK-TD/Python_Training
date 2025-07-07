from rest_framework import serializers
from .models import Drink

class Drinkserlializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']  
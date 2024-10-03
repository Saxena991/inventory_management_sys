from rest_framework import serializers
from .models import UserItem

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserItem
        fields = '__all__'
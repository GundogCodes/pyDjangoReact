from rest_framework import serializers
from .models import User  # Replace with your actual model name

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Replace with your actual model name
        fields = '__all__'  # You can list specific fields instead of '__all__' if needed
from rest_framework import serializers
from .models import mobile


class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = mobile
        fields = '__all__'
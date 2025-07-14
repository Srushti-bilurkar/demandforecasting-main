# demand_forecast/serializers.py
from rest_framework import serializers
from .models import SalesHistory

class SalesHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesHistory
        fields = '__all__'


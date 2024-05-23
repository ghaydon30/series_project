from rest_framework import serializers
from .models import TacoStandFinancialData

# Serializer for TacoStandFinancialData model that includes all fields
class TacoStandFinancialDataSerializer(serializers.ModelSerializer):
    # A nested class that provides metadata about the serializer
    class Meta:
        model = TacoStandFinancialData
        # Includes all fields of the model
        fields = '__all__'

# Serializer for TacoStandFinancialData model for list view with total records
# Mainly to practice more specific fields
class TacoStandFinancialDataListSerializer(serializers.ModelSerializer):
    # Custom field to include the total number of records
    total_records = serializers.SerializerMethodField()
    # A nested class that provides metadata about the serializer
    class Meta:
        model = TacoStandFinancialData
        fields = ['id', 'date', 'daily_revenue', 'daily_customers', 'total_records']

    def get_total_records(self, obj):
        # Method to get full number of total records
        return TacoStandFinancialData.objects.count()
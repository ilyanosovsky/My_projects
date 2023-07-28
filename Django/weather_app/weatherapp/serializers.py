from rest_framework import serializers
from .models import Report, Forecaster

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"

class ForecasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecaster
        fields = "__all__"

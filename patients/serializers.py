from rest_framework import serializers
from .models import Patient, Vitals, VisitFormA, VisitFormB


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class VitalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vitals
        fields = '__all__'
        read_only_fields = ['bmi']  # BMI auto-calculated


class VisitFormASerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitFormA
        fields = '__all__'


class VisitFormBSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitFormB
        fields = '__all__'

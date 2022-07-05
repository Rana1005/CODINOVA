from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    dob = serializers.DateField()
    gender = serializers.CharField(max_length=100)
    imgcheck = serializers.CharField(max_length=100)

    def create(self, validate_data):
        return Patient.objects.create(**validate_data) 
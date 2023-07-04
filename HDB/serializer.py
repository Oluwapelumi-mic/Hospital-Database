from rest_framework import serializers
from .models import Doctor
from .models import Patient
from .models import Medication

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['doctor_id', 'name', 'contact']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [ 'name','card_No', 'ward', 'doctor']

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['name', 'dosage', 'doctor', 'patient']
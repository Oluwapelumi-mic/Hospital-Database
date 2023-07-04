from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    doctor_id = models.IntegerField(max_length=12)
    contact = models.CharField(max_length=255)

    def __str__(self):
        return 'Dr ' + self.name


class Patient(models.Model):
    name = models.CharField(max_length=100)
    card_No = models.IntegerField(max_length=20)
    ward = models.CharField(max_length=6)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return  self.name


class Medication(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return  self.name



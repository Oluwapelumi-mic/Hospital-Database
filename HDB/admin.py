from django.contrib import admin
from .models import Doctor , Patient, Medication

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Medication)
# Register your models here.

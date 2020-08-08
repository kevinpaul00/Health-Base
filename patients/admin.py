from django.contrib import admin
from .models import People, hd, Hospital, MedicalCamp, dependent


myModels = [People, hd, Hospital, MedicalCamp, dependent]
admin.site.register(myModels)

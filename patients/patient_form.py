from django import forms
from . import models 

class CreatePerson(forms.ModelForm):
    class Meta:
        model = models.People
        fields = ['pid', 'pname', 'gender', 'dob', 'phno', 'doorno', 'street', 'area', 'city', 'previous_health_issue', 'hid']

class CreateHospital(forms.ModelForm):
    class Meta:
        model = models.Hospital
        fields = ['hid', 'hname', 'area', 'city', 'hphone']

class CreateDependent(forms.ModelForm):
    class Meta:
        model = models.dependent
        fields = ['dname', 'drelation', 'dph']

class CreateMC(forms.ModelForm):
    class Meta:
        model = models.MedicalCamp1
        fields = ['area', 'hid', 'staffcount']

class CreateHealthIssue(forms.ModelForm):
    class Meta:
        model = models.HealthIssues
        fields = ['issue', 'status']

class CreateMedication(forms.ModelForm):
    class Meta:
        model = models.MedicationTable
        fields = ['Medicine', 'status']
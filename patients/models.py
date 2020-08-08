from django.db import models

# Create your models here.
class Hospital(models.Model):
    hid = models.CharField(max_length=20, primary_key = True)
    hname = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    city  = models.CharField(max_length=200)
    hphone = models.IntegerField(default = 0)

    def __str__(self):
        return self.hname

class Gender1(models.Model):
    gender = models.CharField(max_length=10, primary_key = True)

    def __str__(self):
        return self.gender

class People(models.Model):
    pid = models.IntegerField(default = 0, primary_key = True)
    pname = models.CharField(max_length=200)
    gender = models.ForeignKey(Gender1, on_delete=models.CASCADE)
    dob = models.DateField('date of Birth')
    phno = models.IntegerField(default = 0)
    doorno = models.IntegerField(default=0)
    street = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    previous_health_issue = models.CharField(max_length=200)
    hid = models.ForeignKey(Hospital, on_delete = models.CASCADE)

class hd(models.Model):
    loc = models.CharField(max_length=200, primary_key = True)
    no_of_p = models.IntegerField(default = 0)

class dependent(models.Model):
    pid = models.ForeignKey(People, on_delete = models.CASCADE)
    dname  = models.CharField(max_length=200)
    drelation = models.CharField(max_length=200)
    dph = models.IntegerField(default = 0)

class MedicalCamp(models.Model):
    eid = models.IntegerField(default=0)
    mcloc = models.ForeignKey(hd, on_delete = models.CASCADE)
    campname = models.CharField(max_length=200)

class MedicalCamp1(models.Model):
    area = models.CharField(max_length=200, primary_key = True)
    hid = models.ForeignKey(Hospital, on_delete = models.CASCADE)
    staffcount = models.IntegerField(default=0)

class StatusType(models.Model):
    status = models.CharField(max_length=50, primary_key = True)
    def __str__(self):
        return self.status

class Disease(models.Model):
    issue = models.CharField(max_length=200, primary_key = True)
    risk_type = models.CharField(max_length=200)
    def __str__(self):
        return self.issue

class HealthIssues(models.Model):
    pid = models.ForeignKey(People, on_delete = models.CASCADE)
    issue = models.ForeignKey(Disease, on_delete = models.CASCADE)
    status = models.ForeignKey(StatusType, on_delete=models.CASCADE)
    def __str__(self):
        return self.issue

class MedicineTable(models.Model):
    Medicine = models.CharField(max_length = 100, primary_key = True)
    issue = models.ForeignKey(Disease, on_delete = models.CASCADE)
    def __str__(self):
        return self.Medicine

class MedicationTable(models.Model):
    pid = models.ForeignKey(People, on_delete=models.CASCADE)
    Medicine = models.ForeignKey(MedicineTable, on_delete = models.CASCADE)
    status = models.ForeignKey(StatusType, on_delete = models.CASCADE)


from django.shortcuts import redirect, render
from django.db import connection
from .models import *
from . import patient_form
from django.http import HttpResponse

def patient_list(request):
    #people = People.objects.all()
    people = People.objects.raw('SELECT * FROM patients_people')
    #for p in Person.objects.raw('SELECT * FROM myapp_person'):
    return render(request,'patients/patient_list.html', {'people': people})

def mc_list(request):
    #people = People.objects.all()
    mc = MedicalCamp1.objects.raw('SELECT * FROM patients_medicalcamp1')
    #for p in Person.objects.raw('SELECT * FROM myapp_person'):
    return render(request,'patients/mc_list.html', {'people': mc})

def hospital_list(request):
    hospital = Hospital.objects.raw('SELECT * FROM patients_hospital')
    return render(request,'patients/hospital_list.html', {'hospital': hospital})

def add_patient(request):
    if request.method == 'POST':
        form = patient_form.CreatePerson(request.POST)
        if form.is_valid():
            #Save Patient to db
            #instance = form.save(commit = False)
            #instance.save()
            form.save()
            return redirect('patients:list')
    else:
        form = patient_form.CreatePerson()
    return render(request, 'patients/add_patient.html', {'forms': form})

def add_hospital(request):
    if request.method == 'POST':
        formh = patient_form.CreateHospital(request.POST)
        if formh.is_valid():
            formh.save()
            return redirect('patients:hospital_list')
    else:
        formh = patient_form.CreateHospital()
    
    return render(request, 'patients/add_hospital.html', {'forms': formh})

def add_mc(request):
    if request.method == 'POST':
        form = patient_form.CreateMC(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('patients:risky_cities')
    else:
        form = patient_form.CreateMC()
        
    return render(request, 'patients/add_mc.html', {'forms': form})

def patient_detail(request, pid):  
    patient = People.objects.get(pid = pid)
    dependent1 = dependent.objects.all().filter(pid = patient)
    hi = HealthIssues.objects.all().filter(pid = patient)
    medic = MedicationTable.objects.all().filter(pid = patient)
    #patient = People.objects.raw("SELECT * FROM patients_people WHERE pid = %s", pid)
    return render (request, 'patients/patient_detail.html', {'patient': patient, 'dependent1':dependent1, 'hi':hi, 'medic':medic})

def patient_count(request):
    #count = People.objects.aggregate.raw('SELECT count(*) FROM patients_people')
    count = People.objects.count()
    #count = People.objects.raw('SELECT count(*) as c FROM patients_people')
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM patients_people WHERE gender_id ='Male' ")
    male = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM patients_people WHERE gender_id ='Female' ")
    female = cursor.fetchall()
    return render(request, 'patients/patient_count.html', {'count': count, 'male': male, 'female': female})

def add_dependent(request, pid):
    patient = People.objects.get(pid = pid)
    
    if request.method == 'POST':
        form = patient_form.CreateDependent(request.POST)
        #form.pid = patient.pid
        if form.is_valid():
            #form.pid = patient.pid
            instance = form.save(commit = False)
            instance.pid = patient
            instance.save()
            form.save()
            return redirect('patients:list')
    else:
        form = patient_form.CreateDependent()

    return render(request, 'patients/add_dependent.html', {'forms': form, 'patient':patient})

def add_health_issue(request, pid):
    patient = People.objects.get(pid = pid)
    
    if request.method == 'POST':
        form = patient_form.CreateHealthIssue(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.pid = patient
            instance.save()
            form.save()
            return redirect('patients:list')
    else:
        form = patient_form.CreateHealthIssue()

    return render(request, 'patients/add_healthissue.html', {'forms': form, 'patient':patient})

def add_medication(request, pid):
    patient = People.objects.get(pid = pid)
    
    if request.method == 'POST':
        form = patient_form.CreateMedication(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.pid = patient
            instance.save()
            form.save()
            return redirect('patients:list')
    else:
        form = patient_form.CreateMedication()

    return render(request, 'patients/add_medication.html', {'forms': form, 'patient':patient})

def risky_areas(request):
    cursor = connection.cursor()
    cursor.execute("SELECT area,count(*) as c from patients_people  GROUP BY area ORDER BY count(*) desc;")
    risk = cursor.fetchall()
    return render(request, 'patients/risky_areas.html', {'risk':risk})

def risky_city(request):
    cursor = connection.cursor()
    cursor.execute("SELECT city,count(*) as c from patients_people  GROUP BY city ORDER BY count(*) desc;")
    risk = cursor.fetchall()
    return render(request, 'patients/risky_cities.html', {'risk':risk})

def stats(request):
    cursor = connection.cursor()
    cursor.execute("SELECT Medicine_id,count() from patients_medicationtable inner JOIN patients_people on pid=pid_id GROUP by Medicine_id HAVING status_id = 'Active' order by count() DESC limit 3")
    medWanted = cursor.fetchall()
    
    cursor.execute("SELECT Medicine_id,city,count() from patients_medicationtable inner JOIN patients_people on pid=pid_id GROUP by Medicine_id,city having status_id = 'Active' order by count() DESC limit 3 ")
    medByCity = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM patients_people WHERE (strftime('%Y','now')-strftime('%Y',dob))>40 and gender_id='Male' ")
    oldMale = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM patients_people WHERE (strftime('%Y','now')-strftime('%Y',dob))>40 and gender_id='Female' ")
    oldFemale = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM patients_people WHERE (strftime('%Y','now')-strftime('%Y',dob))>40")
    old = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM patients_people WHERE (strftime('%Y','now')-strftime('%Y',dob))<14 and gender_id='Male' ")
    youngMale = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM patients_people WHERE (strftime('%Y','now')-strftime('%Y',dob))<14 and gender_id='Female' ")
    youngFemale = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM patients_people WHERE (strftime('%Y','now')-strftime('%Y',dob))<14")
    young = cursor.fetchall()



    return render(request, 'patients/stats.html', {'medWanted':medWanted, 'medByCity':medByCity, 'om':oldMale, 'of':oldFemale, 'old':old, 'ym':youngMale, 'yf':youngFemale, 'young':young})

def medicine_requirements(request):
    ps = HealthIssues.objects.annotate(num_comments=models.Count('pid')).all()
    return render(request, 'patients/medicine_requirements.html', {'ps': ps})


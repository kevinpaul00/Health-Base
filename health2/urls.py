
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from . import views
from patients import views as patient_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.homepage, name = "home"),
    url(r'^patients/', include('patients.urls')),
    url(r'^about/$', views.about, name = 'about'),


    path('patients/add-patient/', patient_views.add_patient, name = 'create1'),
    path('patients/patient-count/', patient_views.patient_count, name = 'patientCount'),
    path('patients/',patient_views.patient_list, name="plist"),

    path('patients/add-hospital/', patient_views.add_hospital, name = 'create_hospital'),
    path('patients/risky-areas/', patient_views.risky_areas, name='risky_areas'),
    url('patients/hospital/', patient_views.hospital_list, name="hospital_list"),

    path('patients/risky-areas/', patient_views.risky_areas, name='risky_areas'),
    path('patients/risky-cities/', patient_views.risky_city, name='risky_cities'),
    path('patients/stats-one/', patient_views.risky_city, name='stats'),
    path('patients/medicine-requirements/', patient_views.medicine_requirements, name='medicine_requirements'),

    path('patients/add-camp/', patient_views.add_mc, name = "add_mc"),
    url('patients/mc-list/$', patient_views.mc_list, name="mc_list"),
    

    #url('risky-city/$', patient_views.risky_city, name='risky_cities'),
    #url(r'patients/risky-cities/^(?P<area>[\w-]+)/$', patient_views.add_mc, name = "add_mc"),
]


'''
url(r'^$',views.patient_list, name="list"),
    url(r'^hospital/$', views.hospital_list, name="hospital_list"),
    url(r'^add-patient/$', views.add_patient, name="create"),
    url(r'^add-hospital/$', views.add_hospital, name='create_hospital'),
    url(r'^patient-count/$', views.patient_count, name='patient_count'),
    url(r'^risky-areas/$', views.risky_areas, name='risky_areas'),
    url(r'^(?P<pid>[\w-]+)/$', views.patient_detail, name="detail"),
    url(r'^(?P<pid>[\w-]+)/add-dependent/$', views.add_dependent, name="add_dependent"),
'''
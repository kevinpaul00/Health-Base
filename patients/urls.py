from django.conf.urls import url 
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'patients'

urlpatterns = [
    url(r'^$',views.patient_list, name="list"),
    url(r'^hospital/$', views.hospital_list, name="hospital_list"),
    url(r'^mc-list/$', views.mc_list, name="mc_list"),
    url(r'^add-patient/$', views.add_patient, name="create"),
    url(r'^add-hospital/$', views.add_hospital, name='create_hospital'),
    url(r'^add-camp/$', views.add_mc, name = "add_mc"),
    url(r'^patient-count/$', views.patient_count, name='patient_count'),
    url(r'^risky-areas/$', views.risky_areas, name='risky_areas'),
    url(r'^risky-cities/$', views.risky_city, name='risky_cities'),
    url(r'^stats-one/$', views.stats, name='stats'),
    url(r'^medicine-requirements/$', views.medicine_requirements, name='medicine_requirements'),
    url(r'^(?P<pid>[\w-]+)/$', views.patient_detail, name="detail"),
    

    
    #url(r'^risky-cities/(?P<area>[\w-]+)/$', views.add_mc, name = "add_mc"),
    url(r'^(?P<pid>[\w-]+)/add-dependent/$', views.add_dependent, name="add_dependent"),
    url(r'^(?P<pid>[\w-]+)/add-health-issue/$', views.add_health_issue, name="add_health_issue"),
    url(r'^(?P<pid>[\w-]+)/add-medication/$', views.add_medication, name="add_medication"),
    
]

urlpatterns += staticfiles_urlpatterns()
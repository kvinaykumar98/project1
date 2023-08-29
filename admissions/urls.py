from django.urls import path



from admissions.views import addAdmission
from admissions.views import admissionReport
from admissions.views import malleshPage


urlpatterns = [

    path('newadm/', addAdmission),
    path('admrep/', admissionReport),
    path('mallesh/', malleshPage),

]
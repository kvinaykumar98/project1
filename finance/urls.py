from django.urls import path




from finance.views import feeCollection
from finance.views import feesdueReport
from finance.views import feesCollectionreport




urlpatterns = [


    path('feescoll/', feeCollection),
    path('feesdue/', feesdueReport),
    path('feescollrep/', feesCollectionreport),

]
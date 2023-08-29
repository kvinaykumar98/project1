from django.shortcuts import render



def feeCollection(request):
    return render(request,'finance/fees-collection.html')

def feesdueReport(request):
    return render(request,'finance/feesdue-report.html')


def feesCollectionreport(request):
    return render(request, 'finance/feescollection-report.html')

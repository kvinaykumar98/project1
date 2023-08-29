from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request,'index.html')


def addAdmission(request):
    return render(request,'admissions/add-admission.html.txt')


def admissionReport(request):
    return render(request, 'admissions/admission-report.html.txt')


def malleshPage(request):
    values={'name':'Lover boy mallesh','location':'Bangalore','company':'Novel office'}
    return render(request, 'admissions/mallesh-page.html.txt',values)
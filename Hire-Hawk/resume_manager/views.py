from django.shortcuts import render

# Create your views here.
def testview(request):
    return render(request,'main.html')

def roleview(request):
    return render(request,'roles.html')

def applicantview(request):
    return render(request,'Applicant/AppliDashboard.html')

from django.shortcuts import render,redirect
from .models import Job_description
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.models import User
# Create your views here.

def applicant_view(request):
    jobs = Job_description.objects.all()
    return render(request,'Applicant Updated/AppliDashboard.html',{'jobs': jobs})
        

def job_details_view(request):
    if request.method == "POST":
        job_id = request.POST.get("job_id")
        job = Job_description.objects.get(id = job_id)
        applicant_number = job.applicant_count()
        return render(request,'Applicant Updated/AboutJob.html',{'job': job,'appli_count': applicant_number})


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request,username=email,password = password)
        if user is not None:
            login(request,user)
            return redirect('appview')
        else:
            return redirect('login')
    else:
        return render(request,'Recruiter/RecLogin.html')

def logout_view(request):
    logout(request)

def signup_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        first_name = request.POST.get("name")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirmPassword")
        if( User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists()):
            return redirect('signup')
        else:
            if password == confirm_password:
                user = User.objects.create_user(username =username ,email = email)
                user.set_password(password)
                user.first_name = first_name
                user.save()
                return redirect("appview")
    return render(request,'Recruiter/RecSignup.html')

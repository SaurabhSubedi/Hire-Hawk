from django.shortcuts import render,redirect,reverse
from .models import Job_description,Applicant
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.models import User
from .self_cosine_sim import my_cosine_similarity,read_text
# Create your views here.

def applicant_view(request):
    if request.user.is_authenticated:
        jobs = Job_description.objects.all()
        return render(request,'Applicant Updated/AppliDashboard.html',{'jobs': jobs})
    else:
        return redirect('login')
        

def job_details_view(request):
    if request.method == "POST":
        job_id = request.POST.get("job_id")
        job = Job_description.objects.get(id = job_id)
        applicant_number = job.applicant_count()
        return render(request,'Applicant Updated/AboutJob.html',{'job': job,'appli_count': applicant_number})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('appview')
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
    return redirect('login')

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


def resume_upload(request):
    if request.method == "POST":
        resume = request.FILES['resume']
        current_user = request.user
        job_id = request.POST.get("job_desc")
        job = Job_description.objects.get(id = job_id)
        new_appli = Applicant(user = current_user,job_description= job,resume= resume)
        new_appli.save()
        job_requirement = job.requirement
        resume_text = read_text(new_appli.resume.path)
        score = my_cosine_similarity(job_requirement,resume_text)
        print(score)
        score = score*100
        score = int(score)
        return redirect('score',score=score)
    return redirect('job_desc')
        
def score_view(request,score):
    return render(request,'score_gauge.html',{'score': score})


def admin_all_jobs(request):
    if request.user == is_superuser:
        return render(request, )

    else:
        return redirect('login')


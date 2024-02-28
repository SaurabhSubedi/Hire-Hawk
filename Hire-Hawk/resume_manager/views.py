from django.shortcuts import render,redirect,reverse
from .models import Job_description,Applicant
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.models import User
from .self_cosine_sim import my_cosine_similarity,read_text,jaccards_coefficient
from .utils import skill_extraction
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
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
        job = get_object_or_404(Job_description,id=job_id)
        applicant_number = job.applicant_count()
        text = job.requirement.lower()
        skills = skill_extraction(text)
        cap_skills  = [x.upper() for x in skills ]
        return render(request,'Applicant Updated/AboutJob.html',{'job': job,'appli_count': applicant_number, 'skills': cap_skills})


def login_view(request):
    if request.user.is_superuser:
        return redirect('admin_dashboard')
    if request.user.is_authenticated:
        return redirect('appview')
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request,username=email,password = password)
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect('admin_dashboard')
            return redirect('appview')
        else:
            messages.error(request,"Please enter valid credentials")
            return redirect('login')
    else:
        messages_data = messages.get_messages(request)
        return render(request,'Recruiter/RecLogin.html',{'messages': messages_data})

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
                messages.success(request,"Sign Up Successful.")
                return redirect("appview")
            else:
                messages.error(request,"Passwords didnot match")
                return redirect('signup')
    return render(request,'Recruiter/RecSignup.html')


def resume_upload(request):
    if request.method == "POST":
        resume = request.FILES['resume']
        current_user = request.user
        job_id = request.POST.get("job_desc")
        job = get_object_or_404(Job_description,id=job_id)
        new_appli = Applicant(user = current_user,job_description= job,resume= resume)
        new_appli.save()
        job_requirement = job.requirement
        skill1 = skill_extraction(job_requirement.lower())
        resume_text = read_text(new_appli.resume.path)
        skill2 = skill_extraction(resume_text.lower())
        score = my_cosine_similarity(skill1,skill2)
        score2 = jaccards_coefficient(skill1,skill2)
        final_score = (score+score2)/2
        new_appli.rank = final_score
        new_appli.save()
        final_score = final_score*100
        final_score = int(final_score)
        return redirect('score',score=final_score)
    return redirect('job_desc')
        
def score_view(request,score):
    return render(request,'score_gauge.html',{'score': score})


def admin_all_jobs(request):
    if request.user.is_superuser:
        all_jobs = Job_description.objects.all()
        messages_data = messages.get_messages(request)
        return render(request,'Recruiter/RecDashboard/RecDashboard.html',{'jobs': all_jobs,'messages': messages_data})
    else:
        return redirect('login')

def admin_job_desc(request):
    if request.user.is_superuser:
        if request.method == "POST":
            job_id = request.POST.get("job_id")
            job = get_object_or_404(Job_description,id=job_id)
            applicant_number = job.applicant_count()
            all_applicants = Applicant.objects.filter(job_description=job).order_by('-rank')
            count_applicants = min(3,all_applicants.count())
            top_applicants = all_applicants[:count_applicants]
            text = job.requirement.lower()
            skills = skill_extraction(text)
            cap_skills = [x.capitalize() for x in skills]
            return render(request,'Recruiter/RecDashboard/RecJobDetails.html',{'job': job,'appli_count': applicant_number, 'skills': cap_skills,'applicants':top_applicants})

def admin_job_edit(request):
    if request.user.is_superuser:
        if request.method == "POST":
            job_id = request.POST.get("job_id")
            job = get_object_or_404(Job_description,id=job_id)
            return render(request,'Recruiter/RecDashboard/RecJobEditPage.html',{'job': job})

def job_edit_save(request):
    if request.user.is_superuser:
        if request.method == "POST":
            job_id = request.POST.get("job_id")
            responsibilites = request.POST.get("responsibilities")
            requirements = request.POST.get("requirements")
            salary = request.POST.get("salary")
            job = get_object_or_404(Job_description,id=job_id)
            job.responsibility = responsibilites
            job.requirement = requirements
            job.salary = salary
            job.save()
            messages.success(request,"Job edited successfully")
            return redirect("admin_dashboard")
def about_view(request):
    return render(request, "About.html")

def contactus_view(request):
    if request.user.is_superuser:
        return render(request, "Recruiter/ContactUs.html")

def Acontactus_view(request):
    return render(request, "Applicant Updated/ContactUs.html")

# def profile_view(request):
#     return render(request, "ProfiePage.html")

def userProfile(request):
    return render(request, "Applicant Updated/userProfile.html")

def job_create(request):
    if request.user.is_superuser:
        if request.method == "POST":
            job_title = request.POST.get("job_title")
            salary = request.POST.get("salary")
            responsibilities = request.POST.get("responsibilities")
            requirements = request.POST.get("requirements")
            brief_stat = request.POST.get("brief_stat")
            job = Job_description(title = job_title, brief_stat = brief_stat, responsibility = responsibilities, requirement= requirements,salary = salary)
            job.save()
            messages.success(request,"Job Created Successfully!")
            return redirect("admin_dashboard")
        return render(request,"Recruiter/RecDashboard/RecJobPostPage.html")

def job_delete(request):
    if request.user.is_superuser:
        if request.method=="POST":
            job_id = request.POST.get('job_id')
            job = get_object_or_404(Job_description,id=job_id)
            job.delete()
            messages.success(request,"Job Deleted Successfully")
            return redirect('admin_dashboard')

def dismiss_job(request):
    if request.user.is_superuser:
            if request.method == "GET": 
                job_id = request.GET.get("job_id")
                job = get_object_or_404(Job_description, id=job_id)
                all_applicants = Applicant.objects.filter(job_description=job).order_by('-rank')
                count_applicants = min(3,all_applicants.count())
                top_applicants = all_applicants[:count_applicants]
                top_applicants_email = []
                for applicant in top_applicants:
                        top_applicants_email.append(applicant.user.email)
                context = {
                    'appli_email' :top_applicants_email,
                    'job' :  job,
                }
                return render(request,"Recruiter/RecDashboard/RecEmailWritingPage.html",context)
            if request.method =="POST":
                job_id = request.POST.get("job_id")
                subject = request.POST.get("subject")
                body = request.POST.get("body")
                job = get_object_or_404(Job_description,id=job_id)
                all_applicants = Applicant.objects.filter(job_description=job).order_by('-rank')
                count_applicants = min(3,all_applicants.count())
                top_applicants = all_applicants[:count_applicants]
                top_applicants_email = []
                for applicant in top_applicants:
                    sender_email = settings.EMAIL_HOST_USER
                    receiver = [applicant.user.email]
                    send_mail(subject,body,sender_email,receiver,fail_silently=False)
                    job.delete()
                    messages.success(request,"Email Send Succesfully")
                    return redirect('admin_dashboard')


            
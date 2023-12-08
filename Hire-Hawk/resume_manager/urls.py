from django.urls import path,include
from . import views
urlpatterns = [
    path("", views.login_view, name='login'),
    path("appli/",views.applicant_view,name='appview'),
    path("job_desc/", views.job_details_view,name='job_desc'),
    path("signup/", views.signup_view,name='signup'),
    path("logout/",views.logout_view, name = 'logout'),
    path("resume_upload/",views.resume_upload, name = "resume_upload"),
    path("score_gauge/<int:score>/", views.score_view, name= "score"),
    path("about/", views.about_view, name= "about"),
    path("ContactUs/", views.contactus_view, name= "contactus"),
    path("ProfilePage/", views.profile_view, name= "profile"),
    path("admindash/", views.admin_all_jobs, name= "admin_dashboard"),
    path("adminjobdesc/",views.admin_job_desc,name="admin_job_desc"),
    path("jobedit/", views.admin_job_edit, name="admin_job_edit"),
    path("jobeditsaved/", views.job_edit_save, name="job_edit_save"),
    path("jobcreatepage/",views.job_create, name="job_create"),
    path("jobdelete/",views.job_delete,name="job_delete"),
    path("jobdismiss/",views.job_dismiss,name="job_dismiss"),
]

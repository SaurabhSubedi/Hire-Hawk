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
]

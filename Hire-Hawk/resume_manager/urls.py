from django.urls import path,include
from . import views
urlpatterns = [
    path("", views.login_view, name='login'),
    path("appli/",views.applicant_view,name='appview'),
    path("job_desc/", views.job_details_view,name='job_desc'),
    path("signup/", views.signup_view,name='signup'),
]

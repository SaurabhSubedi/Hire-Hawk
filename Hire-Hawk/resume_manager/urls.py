from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.testview,name='testview'),
    path("roles/",views.roleview, name='roleview'),
    path("appli/",views.applicantview,name='appview'),
]

from django.contrib import admin
from .models import Applicant,Job_description

# Register your models here.
admin.site.register(Applicant)
admin.site.register(Job_description)

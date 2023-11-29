from django.contrib import admin
from .models import Applicant,Job_description,Rank

# Register your models here.
admin.site.register(Applicant)
admin.site.register(Job_description)
admin.site.register(Rank)
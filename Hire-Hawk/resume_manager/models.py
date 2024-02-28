from django.db import models
from django.contrib.auth.models import User

# Models

class Job_description(models.Model):
    title = models.CharField(max_length = 255)
    brief_stat = models.CharField(max_length = 255 ,null = True)
    responsibility = models.TextField()
    requirement = models.TextField()
    salary = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add= True , null = True)
    
    def __str__(self):
        return self.title


    def applicant_count(self):
        return self.applicant_set.count()

    

class Applicant(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    job_description = models.ForeignKey(Job_description, on_delete = models.CASCADE)
    resume = models.FileField(upload_to = 'uploaded_cv/')
    rank = models.FloatField(null= True)
    
    def __str__(self):
        return self.user.email
    

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    cv = models.FileField(upload_to = 'user_cvs/')

    def __str__(self):
        return self.user.email

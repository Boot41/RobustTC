from django.db import models

class Employer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

class JobListing(models.Model):
    employer = models.ForeignKey(Employer, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)
    job_type = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

class JobApplication(models.Model):
    job_listing = models.ForeignKey(JobListing, related_name='applications', on_delete=models.CASCADE)
    seeker_id = models.IntegerField()
    date_applied = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='submitted')
    interview_scheduled = models.BooleanField(default=False)  # New field to track interview schedule status
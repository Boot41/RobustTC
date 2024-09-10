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
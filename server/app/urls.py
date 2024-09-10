from django.urls import path
from .views import create_job, get_jobs, update_job, delete_job

urlpatterns = [
    path('api/jobs', create_job, name='create_job'),
    path('api/employers/<int:employer_id>/jobs', get_jobs, name='get_jobs'),
    path('api/jobs/<int:job_id>', update_job, name='update_job'),
    path('api/jobs/<int:job_id>', delete_job, name='delete_job'),
]
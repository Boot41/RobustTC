from django.urls import path
from .views import create_job, get_jobs, get_job_detail, update_job, delete_job

urlpatterns = [
    path('api/jobs', create_job, name='create_job'),
    path('api/jobs', get_jobs, name='get_jobs'),
    path('api/jobs/<int:job_id>', get_job_detail, name='get_job_detail'),
    path('api/jobs/<int:job_id>', update_job, name='update_job'),
    path('api/jobs/<int:job_id>', delete_job, name='delete_job'),
]
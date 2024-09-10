from django.urls import path
from .views import create_job, get_jobs, get_job_detail, update_job, delete_job, apply_for_job, get_application_status, update_application_status, withdraw_application, get_applications_for_job

urlpatterns = [
    path('api/jobs', create_job, name='create_job'),
    path('api/jobs', get_jobs, name='get_jobs'),
    path('api/jobs/<int:job_id>', get_job_detail, name='get_job_detail'),
    path('api/jobs/<int:job_id>', update_job, name='update_job'),
    path('api/jobs/<int:job_id>', delete_job, name='delete_job'),
    path('api/jobs/<int:job_id>/apply', apply_for_job, name='apply_for_job'),
    path('api/job-seekers/<int:seeker_id>/applications', get_application_status, name='get_application_status'),
    path('api/jobs/<int:job_id>/applications', get_applications_for_job, name='get_applications_for_job'),
    path('api/applications/<int:application_id>/status', update_application_status, name='update_application_status'),
    path('api/applications/<int:application_id>', withdraw_application, name='withdraw_application'),
]
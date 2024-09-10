from django.urls import path
from .views import create_job, get_jobs

urlpatterns = [
    path('api/jobs', create_job, name='create_job'),
    path('api/employers/<int:employer_id>/jobs', get_jobs, name='get_jobs'),
]

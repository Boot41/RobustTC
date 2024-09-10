from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employer, JobListing

class JobListingTests(APITestCase):
    def setUp(self):
        self.employer = Employer.objects.create(name='Test Employer', email='employer@test.com')

    def test_create_job_success(self):
        url = reverse('create_job')
        data = {'employer': self.employer.id, 'title': 'Software Engineer', 'description': 'Develop software', 'location': 'Remote', 'job_type': 'Full-Time'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobListing.objects.count(), 1)
        self.assertEqual(JobListing.objects.get().title, 'Software Engineer')

    def test_create_job_missing_title(self):
        url = reverse('create_job')
        data = {'employer': self.employer.id, 'description': 'Develop software', 'location': 'Remote', 'job_type': 'Full-Time'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_get_jobs_success(self):
        job = JobListing.objects.create(employer=self.employer, title='Backend Developer', description='Work on backend', location='Remote', job_type='Full-Time')
        url = reverse('get_jobs')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Backend Developer')

    def test_get_job_detail_success(self):
        job = JobListing.objects.create(employer=self.employer, title='Backend Developer', description='Work on backend', location='Remote', job_type='Full-Time')
        url = reverse('get_job_detail', args=[job.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Backend Developer')

    def test_get_job_detail_not_found(self):
        url = reverse('get_job_detail', args=[999])  # Non-existent ID
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_jobs_filter_by_title(self):
        job1 = JobListing.objects.create(employer=self.employer, title='Backend Developer', description='Work on backend', location='Remote', job_type='Full-Time')
        job2 = JobListing.objects.create(employer=self.employer, title='Frontend Developer', description='Work on UI', location='Remote', job_type='Part-Time')
        url = reverse('get_jobs') + '?title=Backend'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Backend Developer')

    def test_update_job_success(self):
        job = JobListing.objects.create(employer=self.employer, title='Old Title', description='Description', location='Remote', job_type='Full-Time')
        url = reverse('update_job', args=[job.id])
        data = {'title': 'New Title', 'description': 'Description', 'location': 'Remote', 'job_type': 'Part-Time'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        job.refresh_from_db()
        self.assertEqual(job.title, 'New Title')

    def test_update_job_not_found(self):
        url = reverse('update_job', args=[999])  # Non-existent ID
        data = {'title': 'New Title'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_job_success(self):
        job = JobListing.objects.create(employer=self.employer, title='Job to Delete', description='Description', location='Remote', job_type='Full-Time')
        url = reverse('delete_job', args=[job.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobListing.objects.count(), 0)

    def test_delete_job_not_found(self):
        url = reverse('delete_job', args=[999])  # Non-existent ID
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
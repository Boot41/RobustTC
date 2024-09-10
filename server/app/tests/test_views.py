from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employer, JobListing

class JobListingTests(APITestCase):
    def setUp(self):
        self.employer = Employer.objects.create(name='Test Employer', email='employer@test.com')

    def test_create_job_success(self):
        url = reverse('create_job')
        data = {'employer': self.employer.id, 'title': 'Software Engineer', 'description': 'Develop software', 'location': 'Remote'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobListing.objects.count(), 1)
        self.assertEqual(JobListing.objects.get().title, 'Software Engineer')

    def test_create_job_missing_title(self):
        url = reverse('create_job')
        data = {'employer': self.employer.id, 'description': 'Develop software', 'location': 'Remote'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_jobs_success(self):
        job = JobListing.objects.create(employer=self.employer, title='Backend Developer', description='Work on backend', location='Remote')
        url = reverse('get_jobs', args=[self.employer.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Backend Developer')

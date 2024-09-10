from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employer, JobListing, JobApplication

class JobApplicationTests(APITestCase):
    def setUp(self):
        self.employer = Employer.objects.create(name='Test Employer', email='employer@test.com')
        self.job_listing = JobListing.objects.create(employer=self.employer, title='Software Engineer', description='Develop software', location='Remote', job_type='Full-Time')

    def test_apply_for_job_success(self):
        url = reverse('apply_for_job', args=[self.job_listing.id])
        data = {'seeker_id': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobApplication.objects.count(), 1)
        self.assertEqual(JobApplication.objects.first().job_listing, self.job_listing)

    def test_apply_for_job_job_not_found(self):
        url = reverse('apply_for_job', args=[999])  # Non-existent Job ID
        data = {'seeker_id': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_apply_for_job_validation_error(self):
        url = reverse('apply_for_job', args=[self.job_listing.id])
        data = {}  # Missing seeker_id
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_application_status_success(self):
        application = JobApplication.objects.create(job_listing=self.job_listing, seeker_id=1)
        url = reverse('get_application_status', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['seeker_id'], 1)

    def test_get_application_status_no_applications(self):
        url = reverse('get_application_status', args=[999])  # Non-existent seeker_id
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)  # No applications

    def test_get_applications_for_job_success(self):
        application1 = JobApplication.objects.create(job_listing=self.job_listing, seeker_id=1)
        application2 = JobApplication.objects.create(job_listing=self.job_listing, seeker_id=2)
        url = reverse('get_applications_for_job', args=[self.job_listing.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_application_status_success(self):
        application = JobApplication.objects.create(job_listing=self.job_listing, seeker_id=1)
        url = reverse('update_application_status', args=[application.id])
        data = {'status': 'under_review'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        application.refresh_from_db()
        self.assertEqual(application.status, 'under_review')

    def test_update_application_status_not_found(self):
        url = reverse('update_application_status', args=[999])  # Non-existent Application ID
        data = {'status': 'under_review'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_withdraw_application_success(self):
        application = JobApplication.objects.create(job_listing=self.job_listing, seeker_id=1)
        url = reverse('withdraw_application', args=[application.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobApplication.objects.count(), 0)

    def test_withdraw_application_not_found(self):
        url = reverse('withdraw_application', args=[999])  # Non-existent Application ID
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
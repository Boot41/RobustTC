from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employer, JobListing, JobApplication, JobSeekerProfile

class JobApplicationTests(APITestCase):
    # Existing tests...

class JobSeekerProfileTests(APITestCase):
    def setUp(self):
        self.profile_data = {'seeker_id': 1, 'work_history': 'Software Engineer at XYZ', 'skills': 'Python, Django', 'education': 'Bachelor in Computer Science'}

    def test_create_job_seeker_profile_success(self):
        url = reverse('create_job_seeker_profile')
        response = self.client.post(url, self.profile_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobSeekerProfile.objects.count(), 1)
        self.assertEqual(JobSeekerProfile.objects.get().seeker_id, 1)

    def test_create_job_seeker_profile_validation_error(self):
        url = reverse('create_job_seeker_profile')
        response = self.client.post(url, {}, format='json')  # Invalid data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_job_seeker_profile_success(self):
        JobSeekerProfile.objects.create(**self.profile_data)
        url = reverse('get_job_seeker_profile', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['seeker_id'], 1)

    def test_get_job_seeker_profile_not_found(self):
        url = reverse('get_job_seeker_profile', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_job_seeker_profile_success(self):
        JobSeekerProfile.objects.create(**self.profile_data)
        url = reverse('update_job_seeker_profile', args=[1])
        updated_data = {'skills': 'Python, Django, REST'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(JobSeekerProfile.objects.get(seeker_id=1).skills, 'Python, Django, REST')

    def test_update_job_seeker_profile_not_found(self):
        url = reverse('update_job_seeker_profile', args=[999])
        response = self.client.put(url, {'skills': 'Python'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

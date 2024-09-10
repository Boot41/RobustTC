from django.test import TestCase
from .models import Employer, JobListing, JobApplication

class JobApplicationModelTest(TestCase):
    def setUp(self):
        self.employer = Employer.objects.create(name='Test Employer', email='employer@test.com')
        self.job_listing = JobListing.objects.create(employer=self.employer, title='Data Scientist', description='Analyze data', location='Remote', job_type='Full-Time')
        self.application = JobApplication.objects.create(job_listing=self.job_listing, seeker_id=1)

    def test_job_application_fields(self):
        self.assertEqual(self.application.job_listing, self.job_listing)
        self.assertEqual(self.application.seeker_id, 1)
        self.assertTrue(self.application.date_applied is not None)
        self.assertEqual(self.application.status, 'submitted')
        
    def test_job_application_str(self):
        self.assertEqual(str(self.application), f'JobApplication: {self.application.job_listing.title} by {self.application.seeker_id}')

    def test_application_creation_with_invalid_data(self):
        with self.assertRaises(ValueError):
            JobApplication.objects.create(job_listing=None, seeker_id=1)  # Invalid Job Listing
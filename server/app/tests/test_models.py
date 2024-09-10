from django.test import TestCase
from .models import Employer, JobListing

class JobListingModelTest(TestCase):
    def setUp(self):
        self.employer = Employer.objects.create(name='Test Employer', email='employer@test.com')
        self.job = JobListing.objects.create(employer=self.employer, title='Data Scientist', description='Analyze data', location='Remote')

    def test_job_listing_fields(self):
        self.assertEqual(self.job.title, 'Data Scientist')
        self.assertEqual(self.job.description, 'Analyze data')
        self.assertEqual(self.job.location, 'Remote')
        self.assertTrue(self.job.is_active)

    def test_job_listing_employer_relationship(self):
        self.assertEqual(self.job.employer, self.employer)

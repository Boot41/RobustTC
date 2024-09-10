from django.test import TestCase
from .models import Employer, JobListing, JobApplication

class JobApplicationModelTest(TestCase):
    def setUp(self):
        self.employer = Employer.objects.create(name='Test Employer', email='employer@test.com')
        self.job_listing = JobListing.objects.create(employer=self.employer, title='Data Scientist', description='Analyze data', location='Remote', job_type='Full-Time')

    def test_job_application_fields(self):
        application = JobApplication.objects.create(job_listing=self.job_listing, seeker_id=1)
        self.assertEqual(application.job_listing, self.job_listing)
        self.assertEqual(application.seeker_id, 1)
        self.assertTrue(application.date_applied is not None)
        self.assertEqual(application.status, 'submitted')
        self.assertFalse(application.interview_scheduled)  # Newly added assert for interview_scheduled
        
    def test_job_application_str(self):
        application = JobApplication.objects.create(job_listing=self.job_listing, seeker_id=1)
        self.assertEqual(str(application), f'JobApplication: {application.job_listing.title} by {application.seeker_id}')

    def test_application_creation_with_invalid_data(self):
        with self.assertRaises(ValueError):
            JobApplication.objects.create(job_listing=None, seeker_id=1)  # Invalid Job Listing

    def test_update_interview_scheduled_field(self):
        application = JobApplication.objects.create(job_listing=self.job_listing, seeker_id=1)
        application.interview_scheduled = True
        application.save()
        self.assertTrue(application.interview_scheduled)
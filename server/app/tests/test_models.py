from django.test import TestCase
from .models import Employer, JobListing, JobApplication, JobSeekerProfile

class JobApplicationModelTest(TestCase):
    # Existing tests...

class JobSeekerProfileModelTest(TestCase):
    def test_job_seeker_profile_creation(self):
        profile = JobSeekerProfile.objects.create(seeker_id=1, work_history='Data Analyst at ABC', skills='SQL, R', education='Master in Data Science')
        self.assertEqual(profile.seeker_id, 1)
        self.assertEqual(profile.work_history, 'Data Analyst at ABC')
        self.assertEqual(profile.skills, 'SQL, R')
        self.assertEqual(profile.education, 'Master in Data Science')
        self.assertTrue(profile.date_updated is not None)

    def test_job_seeker_profile_str(self):
        profile = JobSeekerProfile(seeker_id=1)
        self.assertEqual(str(profile), f'Profile of Seeker ID {profile.seeker_id}')  # Ensure this matches your model's str method

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Job_description, Applicant

class YourAppTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.job = Job_description.objects.create(title='Test Job', responsibility='Test Responsibility', requirement='Test Requirement', salary='Test Salary')

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'email': 'testuser@example.com', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)

    def test_applicant_view_authenticated(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('appview'))
        self.assertEqual(response.status_code, 200)

    def test_applicant_view_unauthenticated(self):
        response = self.client.get(reverse('appview'))
        self.assertEqual(response.status_code, 302)

    def test_job_details_view(self):
        response = self.client.post(reverse('job_desc'), {'job_id': self.job.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Job')

    def test_signup_view(self):
        response = self.client.post(reverse('signup'), {'email': 'newuser@example.com', 'username': 'newuser', 'name': 'New User', 'password': 'newpassword', 'confirmPassword': 'newpassword'})
        self.assertEqual(response.status_code, 302)


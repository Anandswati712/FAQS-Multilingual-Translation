import pytest
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APITestCase
from storeFAQ.models import FAQ

@pytest.fixture
def client():
    return APIClient()

        

class FAQApiTest(APITestCase):
    
    def setUp(self):
        if not FAQ.objects.filter(question="What is Django?").exists():
            FAQ.objects.create(question="What is Django?", answer="Django is a web framework written in Python.")
        
        if not FAQ.objects.filter(question="What is Python?").exists():
            FAQ.objects.create(question="What is Python?", answer="Python is a programming language.")

    def test_faq_api(self):
        response = self.client.get('/api/faqs/?lang=es')
        response.status_code == status.HTTP_200_OK
        self.assertGreater(len(response.data), 0)  
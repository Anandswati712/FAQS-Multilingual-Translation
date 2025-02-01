import pytest
from storeFAQ.models import FAQ

@pytest.mark.django_db
def test_faq_translation():
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework written in Python."
    )

    translated_text = faq.get_translated_question("hi")  
    assert translated_text != "What is Django?"  # Ensure it's translated

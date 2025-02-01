from storeFAQ.models import FAQ

faqs = [
    {"question": "What is Django?", "answer": "Django is a web framework written in Python."},
    {"question": "How does Django handle security?", "answer": "Django has built-in security features to protect against attacks like SQL Injection."},
    {"question": "What databases does Django support?", "answer": "Django supports SQLite, PostgreSQL, MySQL, and Oracle."}
]

for data in faqs:
    faq = FAQ.objects.create(question=data["question"], answer=data["answer"])
    faq.save()

print("FAQs have been successfully populated!")
faq_objects = FAQ.objects.all()
for faq in faq_objects:
    print(f"Question: {faq.question}")
    print(f"Answer: {faq.answer}")
    print("-" * 50)
# **Multilingual FAQ API**  

A Django-based REST API for storing, managing, and retrieving FAQs with multi-language translation support.

## **Table of Contents**  
- [Features](#features)  
- [Installation](#installation)  
- [Project Structure](#project-structure)  
- [Configuration](#configuration)  
- [Running the Application](#running-the-application)  
- [API Usage](#api-usage)  
- [Docker Support](#docker-support)  
- [Testing](#testing)  
- [Contribution Guidelines](#contribution-guidelines)  
- [License](#license)  

---

## **Features**  
✅ Store FAQs with questions and answers.  
✅ Retrieve FAQs dynamically with multi-language translation support.  
✅ Supports database caching for optimized performance.  
✅ RESTful API with Django REST Framework (DRF).  
✅ Dockerized setup for easy deployment.  
✅ Supports PostgreSQL, MySQL, and SQLite.  

---

## **Installation**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/Anandswati712/faq-multilingual-translation.git  
 
```

### **2. Set Up a Virtual Environment**  
```bash
python3 -m venv venv  
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt  
```

### **4. Configure Environment Variables**  
Rename `.env.example` to `.env` and update the following variables:  
```ini
DJANGO_SECRET_KEY=your-secret-key  
DEBUG=True  
DB_NAME=faq_db  
DB_USER=your_db_user  
DB_PASSWORD=your_db_password  
DB_HOST=localhost  
DB_PORT=5432  
```

### **5. Apply Migrations**  
```bash
python manage.py migrate  
```

### **6. Create a Superuser (Optional)**  
```bash
python manage.py createsuperuser  
```

### **7. Run the Development Server**  
```bash
python manage.py runserver  
```
The API will be available at: `http://127.0.0.1:8000/api/faqs/`

---

## **Project Structure**  

```
multilingual-faq-api/  
│── storeFAQ/                # Django app for FAQ management  
│   │── migrations/           # Database migrations  
│   │── templates/            # HTML templates (if applicable)  
│   │── admin.py              # Django admin panel configuration  
│   │── models.py             # FAQ model definition  
│   │── serializers.py        # Serializers for API responses  
│   │── urls.py               # API endpoint definitions  
│   │── views.py              # API view logic  
│   │── unit_tests.py         # Unit tests for the app
|   |── populate_faqs.py      #create and store FAQs
│── BharatFD/                    # Main project settings  
│   │── settings.py           # Django settings  
│   │── urls.py               # Project-wide URL routing  
│   │── wsgi.py               # WSGI entry point  
│   │── asgi.py               # ASGI entry point  
│── static/                  # Static files (CSS, JavaScript, etc.)  
│── templates/               # Project-wide templates  
│── Dockerfile               # Docker configuration for containerization  
│── docker-compose.yml       # Docker Compose file for multi-container setup  
│── manage.py                # Django management script  
│── requirements.txt         # Dependencies list  
│── .gitignore               # Git ignore file  
│── README.md                # Project documentation  
```

---

## **Configuration**  

Modify `settings.py` to customize:  
- Allowed hosts: `ALLOWED_HOSTS`  
- Database settings  
- CORS support  
- Translation settings  

---

## **API Usage**  

### **1. Get All FAQs**  
**Endpoint:**  
```http
GET /api/faqs/  
```
**Response:**  
```json
[
    {
        "question": "What is Django?",
        "answer": "Django is a Python framework."
    },
    {
        "question": "How does Django handle security?",
        "answer": "Django has built-in security features."
    }
]
```

### **2. Get FAQs in a Specific Language**  
**Endpoint:**  
```http
GET /api/faqs/?lang=fr  
```
**Response:**  
```json
[
    {
        "question": "Qu'est-ce que Django?",
        "answer": "Django est un framework Python."
    }
]
```

### **3. Create a New FAQ**  
**Endpoint:**  
```http
POST /api/faqs/  
```
**Payload:**  
```json
{
    "question": "What databases does Django support?",
    "answer": "Django supports PostgreSQL, MySQL, SQLite, and Oracle."
}
```
**Response:**  
```json
{
    "id": 3,
    "question": "What databases does Django support?",
    "answer": "Django supports PostgreSQL, MySQL, SQLite, and Oracle."
}
```

---

## **Docker Support**  

### **1. Build and Run the Docker Container**  
```bash
docker-compose up --build  
```

### **2. Run Migrations in Docker**  
```bash
docker exec -it web python manage.py migrate  
```

### **3. Stop the Container**  
```bash
docker-compose down  
```

---

## **Testing**  
Run the test suite using:  
```bash
pytest  
```
or  
```bash
python manage.py test  
```

---

## **Contribution Guidelines**  
We welcome contributions! 🚀 Follow these steps to contribute:  

1. **Fork the Repository**:  
   Click the "Fork" button on GitHub.  

2. **Clone Your Fork**:  
   ```bash
   git clone https://github.com/Anandswati712/faq-multilingual-translation.git  
   cd BharatFD 
   ```

3. **Create a Feature Branch**:  
   ```bash
   git checkout -b feature-new-api-endpoint  
   ```

4. **Commit Changes**:  
   Follow conventional commit messages:  
   ```bash
   git commit -m "feat: Add support for French translations"  
   ```

5. **Push to Your Branch**:  
   ```bash
   git push origin feature-new-api-endpoint  
   ```

6. **Create a Pull Request (PR)**:  
   Go to GitHub and open a **Pull Request** from your forked repository.  

---

## **License**  
This project is licensed under the **MIT License**. Feel free to use and modify it.  

---

# Use an official Python runtime as the base image
FROM python:3.10-slim

# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#     libpq-dev \
#     build-essential \
#     libffi-dev \
#     libssl-dev \
#     && rm -rf /var/lib/apt/lists/*
# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . /app/

# Expose the port the app will run on
EXPOSE 8000

# Run migrations and start the Django app
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

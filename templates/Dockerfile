# Use Python 3.9 slim as the base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy only necessary files first to leverage Docker caching
COPY requirements.txt /app/

# Install system dependencies and fix Hash Sum mismatch
RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . /app/

# Expose the port the Django app runs on
EXPOSE 8000

# Command to run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . /app/

# Install system dependencies
RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

# Install Python dependencies from requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose the port for Django
EXPOSE 8000

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

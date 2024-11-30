# Use an official Python 3.12 image as a parent image
FROM python:3.12.0-slim

# Set environment variable to prevent writing bytecode files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port that Django will run on
EXPOSE 8000

# Set the command to run your Django app (replace with your actual command)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

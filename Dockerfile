# Use the official Python image
FROM python:3.11.3

# Set the working directory
WORKDIR /app

# Copy the files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Flask application
CMD ["python", "server.py"]

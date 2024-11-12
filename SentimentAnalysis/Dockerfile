# Use the official Python image
FROM python:3.11.3

# Set the working directory
WORKDIR /module

# Copy the files into the container
COPY . /module

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the sentiment analysis script (modify as needed)
CMD ["python", "sentiment_analysis.py"]

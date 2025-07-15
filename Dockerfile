# Dockerfile

# Base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the project files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port Flask will run on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]

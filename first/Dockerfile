FROM python:3.12-slim

# Set the working directory in the image
WORKDIR /app

# Copy the files from the host file system to the image file system
COPY . /app

# Set environment variables
ENV NAME World

# Run a command to start the application
CMD ["python3", "app.py"]

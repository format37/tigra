# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir flask

# Make port 6000 available to the world outside this container
# EXPOSE 6000

# Run server.py when the container launches
CMD ["python", "server.py"]

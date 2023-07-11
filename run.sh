#!/bin/bash

# Create the logs directory if it does not exist
mkdir -p logs

# Run the Docker container, mounting the logs directory
# docker run -p 5000:5000 -v $(pwd)/logs:/app/logs flask-server:latest
docker run --network=host -v $(pwd)/logs:/app/logs tigra-server:latest

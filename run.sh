#!/bin/bash

# Create the logs directory if it does not exist
mkdir -p logs

# Run the Docker container, mounting the logs directory
sudo docker run --network=host -v $(pwd)/logs:/app/logs tigra-server:latest

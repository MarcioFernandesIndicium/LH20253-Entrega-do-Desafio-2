# Dockerfile for Meltano project with Databricks CLI setup
# Use the official Meltano image as the base
ARG MELTANO_IMAGE=meltano/meltano:latest-python3.11
FROM $MELTANO_IMAGE

# Install dependencies
RUN apt update && \
    apt install -y curl && \
    apt install -y unzip

# Install Databricks CLI
RUN curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh

# Create a directory for the Meltano project
WORKDIR /projects/meltano-api

# Copy the Meltano project files into the container
COPY . .

# Install Python dependencies
RUN pip install -e .

# Run Meltano commands to set up the project
RUN meltano lock --update --all && \
    meltano install

# Set entrypoint to run Meltano commands   
#ENTRYPOINT [ "/bin/bash", "-c"]
ENTRYPOINT [ "./entrypoint.sh"]
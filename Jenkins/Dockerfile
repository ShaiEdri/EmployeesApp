# We are extending everything from jenkins/jenkins:lts image.
FROM jenkins/jenkins:lts

# Switch to root to install docker and docker compose
USER root

# Install necessary dependencies
RUN apt-get update && \
    apt-get -y install apt-transport-https \
         ca-certificates \
         curl \
         gnupg2 \
         software-properties-common

# Download and add Docker's official GPG key
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -

# Add Docker's stable repository
RUN add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/debian \
    $(lsb_release -cs) \
    stable"

# Update the package database and install Docker
RUN apt-get update && \
    apt-get -y install docker-ce

# Add jenkins user to docker group
RUN usermod -aG docker jenkins

# Install Docker Compose
ENV DOCKER_COMPOSE_VERSION 1.29.2
RUN curl -L "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

# Switch back to jenkins user
USER jenkins
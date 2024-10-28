# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /tests

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    default-jre \
    && rm -rf /var/lib/apt/lists/*

# Install Allure commandline
RUN wget https://github.com/allure-framework/allure2/releases/download/2.24.1/allure-2.24.1.zip \
    && unzip allure-2.24.1.zip -d /opt \
    && rm allure-2.24.1.zip \
    && ln -s /opt/allure-2.24.1/bin/allure /usr/local/bin/allure

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install chromium \
    && playwright install-deps chromium

# Copy test files
COPY . .

# Create directories for reports
RUN mkdir -p allure-results allure-reports

# Create entrypoint script
RUN echo '#!/bin/bash\n\
pytest --alluredir=allure-results\n\
allure generate allure-results -o allure-reports --clean\n\
allure open allure-reports -p 8080 -h 0.0.0.0\n\
' > /entrypoint.sh \
    && chmod +x /entrypoint.sh

# Expose port for Allure reports
EXPOSE 8080

# Set entrypoint
ENTRYPOINT ["/entrypoint.sh"]

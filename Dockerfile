# Use a general Python image (you can choose a specific version tag)
FROM python:3.9

# Set the working directory
WORKDIR /app

# Install system dependencies 
RUN apt-get update && apt-get install -y \
    chromium=128.0.6613.84 \
    wget \
    unzip \
    xvfb  \
    python3-pip

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Manually install ChromeDriver ---
# Get the latest ChromeDriver version (replace with actual latest version)
RUN wget https://storage.googleapis.com/chrome-for-testing-public/128.0.6613.84/linux64/chromedriver-linux64.zip

# Unzip the ChromeDriver archive
RUN unzip chromedriver-linux64.zip

# Make ChromeDriver executable
RUN chmod +x chromedriver-linux64/chromedriver

# Move ChromeDriver to a location in the PATH
RUN mv chromedriver-linux64/chromedriver /bin

# --- End of ChromeDriver installation ---

# Copy your application code
COPY app.py .

# Set the DISPLAY environment variable for headless Chrome
ENV DISPLAY=:99

# Run Xvfb in the background (needed for headless Chrome)
CMD Xvfb :99 -screen 0 1024x768x24 & python3 app.py
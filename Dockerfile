# Use official slim Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY app.py .

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

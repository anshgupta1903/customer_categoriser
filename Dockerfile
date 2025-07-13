# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first (so Docker can cache deps)
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port (FastAPI default)
EXPOSE 8000

# Command to run the API
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]

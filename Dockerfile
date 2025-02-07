# Use an official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy necessary files
COPY requirements.txt .
COPY app.py .
COPY artifacts/ /app/artifacts/

# Install dependencies
RUN pip install -r requirements.txt

# Expose the FastAPI port (default 8000)
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]


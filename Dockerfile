# Use Python 3.8 slim version as the base image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install curl
RUN apt-get update && apt-get install -y curl

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Expose the port that FastAPI runs on
EXPOSE 8000

# Command to run the Ollama server and then execute "ollama run llama2"
CMD ["sh", "-c", "ollama serve & sleep 25 && ollama run llama2 && uvicorn main:app --host 0.0.0.0 --port 8000"]

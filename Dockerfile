# Use the official Python base image
FROM pytorch/pytorch:latest

# Set the working directory inside the container
WORKDIR ./

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 8090

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

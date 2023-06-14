# Use a base image suitable for your application
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the working directory
COPY deploy/ .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set any necessary environment variables
EXPOSE 5000
ENV PORT 5000


# Specify the command to run your application
# Use gunicorn as the entrypoint
CMD exec gunicorn --bind :$PORT app:app --workers 1 --threads 1 --timeout 60

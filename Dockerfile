# Use a base image suitable for your application
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the working directory
COPY deploy/ .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set any necessary environment variables

# Expose the port on which your application will run (if applicable)
EXPOSE 8080

# Specify the command to run your application
CMD [ "python", "app.py" ]

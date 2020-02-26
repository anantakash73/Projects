# Use an official Python runtim
FROM python:3.6.9-stretch

# Set working directory to /app
WORKDIR /app

# Copy current directory into container at /app
COPY . /app

# Install any needed packages
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available
EXPOSE 8080

# Run app.py when the container launches
CMD ["python3","app.py"]
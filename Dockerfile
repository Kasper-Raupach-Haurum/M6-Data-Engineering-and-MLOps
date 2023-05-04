# Use an official Python runtime as a parent image
FROM python:3.9

 

# Update package list and install sudo
RUN apt-get update && apt-get install -y sudo

 

# Set the working directory
WORKDIR /app

 

# Copy the requirements file into the container
COPY requirements.txt /app

 

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

 

# Copy the rest of the application code
COPY . /app

 

# Make the script executable
RUN chmod +x /app/M6_Data_Engineering_and_MLOps_Assignment_4_appfile.py

 

# Expose the port for Streamlit
EXPOSE 8501

 

# Run the Streamlit app when the container launches
ENTRYPOINT ["streamlit", "run", "M6_Data_Engineering_and_MLOps_Assignment_4_appfile.py", "--server.port", "8501", "--server.address", "0.0.0.0"]

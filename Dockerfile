# set base layer
FROM python:3.12-slim

# set working dir in container
WORKDIR /usr/src/app

# copy over requirements file
COPY requirements.txt ./

# Install python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# copy main python script
COPY app.py ./app.py

COPY templates ./templates

# Copy the entrypoint script and make it executable
RUN chmod +x app.py

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run app.py when the container launches
CMD ["python", "app.py"]


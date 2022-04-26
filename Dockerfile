FROM python:3.9

# Install dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Copy application code
COPY ./app /app/

WORKDIR /

# Set the entrypoint
CMD python app/api.py
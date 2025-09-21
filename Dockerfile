FROM python:3.11-slim

# Install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY basic-auth.py .

# Default data directory
VOLUME /data

# Expose port (default 8080, overridable at runtime)
EXPOSE 8080

CMD ["python", "basic-auth.py"]

# Use Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest
COPY . .

# Expose backend port
EXPOSE 3838

# TODO Run flask app
CMD ["./blog_api/entrypoint.sh"]
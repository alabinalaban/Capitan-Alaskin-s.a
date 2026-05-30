FROM python:3.9-slim

# Set a non‑root user for security
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Set the working directory
WORKDIR /app

# Install system dependencies (if any) – none required for this project
# Copy only needed files (exclude local caches with .dockerignore)
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose nothing (the bot connects outwards)

# Default command to run the bot
CMD ["python", "bot.py"]

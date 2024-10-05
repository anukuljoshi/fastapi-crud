FROM python:3.12-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:0.4.18 /uv /bin/uv

# Copy the application into the container.
COPY . /usr/src/app

# Install the application dependencies.
WORKDIR /usr/src/app
RUN uv sync --frozen --no-cache

# Run the application.
CMD ["/app/.venv/bin/fastapi", "run", "app/main.py", "--port", "80", "--host", "0.0.0.0"]

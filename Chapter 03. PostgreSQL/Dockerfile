FROM python:3.11.8-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

# Install PostgreSQL client libraries for psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . .


FROM python:3.11-slim

RUN apt-get update && apt-get install -y             build-essential             libssl-dev             libffi-dev             libcurl4-openssl-dev             libexpat1-dev             pkg-config             cmake             git             libgit2-dev          && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
ENV PYTHONUNBUFFERED=1

ENV GIT_REPOS_ROOT=/data/git
RUN mkdir -p ${GIT_REPOS_ROOT} && chown -R 1000:1000 ${GIT_REPOS_ROOT}
VOLUME ["/data"]

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000", "--workers","4"]

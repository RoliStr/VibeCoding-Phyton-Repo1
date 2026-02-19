FROM python:3.12-slim

WORKDIR /app
COPY pyproject.toml /app/pyproject.toml
COPY src/ /app/src/

# keine extra deps nötig, aber wir setzen PYTHONPATH sauber
ENV PYTHONPATH=/app/src

ENTRYPOINT ["python", "-m", "myapp.cli"]

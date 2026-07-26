FROM python:3.13-alpine

COPY --from=ghcr.io/astral-sh/uv:python3.13-alpine /uv /uvx /bin/

LABEL authors="amirhosseinmohammadi"

WORKDIR /app

COPY . .

RUN uv sync --locked

CMD ["uv", "run", "main.py"]
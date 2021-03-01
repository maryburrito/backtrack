FROM python:3.8.8

EXPOSE 8000

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.4

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-dev

COPY ./backtrack ./backtrack
COPY ./tracker ./tracker
COPY ./templates ./templates
COPY ./scripts ./scripts
COPY ./manage.py .

CMD ["/app/scripts/server"]

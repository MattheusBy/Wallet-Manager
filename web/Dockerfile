FROM python:3.10

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
COPY . .
RUN apt-get update
RUN pip install --user poetry
ENV PATH="${PATH}:/root/.local/bin"
RUN poetry install
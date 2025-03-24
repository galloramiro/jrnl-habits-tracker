FROM python:3.11.4-bullseye

WORKDIR /app

# Installing dependencies
RUN pip install --user poetry
ENV PATH="/root/.local/bin:/app/examples/scripts:${PATH}"

COPY poetry.lock /app/
COPY pyproject.toml /app/
COPY logging.conf /app/
COPY examples/.jrnl.cfg /root/

RUN poetry lock
RUN poetry install

# Copy core project
COPY src /app/src


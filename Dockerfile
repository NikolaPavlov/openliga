FROM python


ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN pip install poetry

COPY ./website /app
WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction


COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]


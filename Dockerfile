FROM python:3.13

RUN pip install poetry

WORKDIR /marketplace

COPY pyproject.toml poetry.lock /marketplace/

RUN poetry install --no-root

COPY . /marketplace

CMD ["poetry", "run", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
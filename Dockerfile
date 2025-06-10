FROM python:3.13

RUN pip install poetry

WORKDIR /marketplace

COPY pyproject.toml poetry.lock /marketplace/

RUN poetry install --no-root

COPY . .

CMD ["python", "main.py"]

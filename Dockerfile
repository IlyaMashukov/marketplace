FROM python:3.13

RUN mkdir -p /marketplace
WORKDIR /marketplace

COPY . /marketplace
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]


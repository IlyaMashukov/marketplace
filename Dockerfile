FROM python:3.13

WORKDIR /marketplace

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]


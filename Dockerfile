FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY test_app.py .

RUN python -m unittest test_app -v

CMD ["python", "app.py"]

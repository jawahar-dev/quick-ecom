FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Install mysql-client
RUN apt-get update && apt-get install -y default-mysql-client

COPY . .

CMD ["python3", "app.py"]

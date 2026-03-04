#This is test for my git-webhook.
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV SECRET_KEY=career_app_secret

CMD ["python", "app.py"]

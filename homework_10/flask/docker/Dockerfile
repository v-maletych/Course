FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["./wait-for-it.sh", "db:3306", "--", "python", "app.py"]

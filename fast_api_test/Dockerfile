FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /

RUN apt-get update && apt-get install -y ffmpeg gettext vim

EXPOSE 8080

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

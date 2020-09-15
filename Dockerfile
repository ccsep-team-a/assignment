FROM python:3.8.2-alpine as build
LABEL maintainer jactacular
RUN apk --update add build-base 
COPY src/ /app
WORKDIR /app
RUN pip install -r requirements.txt

ENV FLASK_APP app.py

CMD [ "python", "-m", \
    "flask", "run", \
    "-p", "8000", \
    "-h", "0.0.0.0"\
    ]

# Base build with requirements installed
FROM python:3.8.2-alpine as build
LABEL maintainer jactacular

RUN apk --update add build-base 
# Create app directory 
RUN mkdir /app
WORKDIR /app
COPY src/requirements.txt .
# install app dependencies
RUN pip install -r requirements.txt --disable-pip-version-check

COPY src/ .


# TODO: Move tests to seperate docker image
    # COPY test/requirements.txt >> /app/requirements.txt
COPY test/ /app

# FROM python:3.8.2-alpine
ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV development
ENV FLASK_APP app.py
# WORKDIR /app
# COPY  /app .
# COPY --from=build /root/.local /root/.local
EXPOSE 8000
CMD [ "python", "-m", \
    "flask", "run", \
    "-p", "8000", \
    "-h", "0.0.0.0"\
    ]

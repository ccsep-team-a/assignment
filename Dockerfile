# Base build with dev and test requirements installed
FROM python:3.8.2-alpine as dev-build
LABEL maintainer jactapular

RUN apk --update add build-base 

# Create app directory 
RUN mkdir /app
WORKDIR /app
COPY src/requirements.txt .

# install app dependencies
RUN pip install -r requirements.txt --disable-pip-version-check

# copy source files
COPY src/ .

# copy test files
COPY test/ /app

ENV FLASK_ENV development
ENV FLASK_APP app.py

EXPOSE 8000
CMD [ "python", "-m", \
    "flask", "run", \
    "-p", "8000", \
    "-h", "0.0.0.0"\
    ]

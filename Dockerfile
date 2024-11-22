FROM python:3.14-rc-alpine3.20
LABEL maintainer="abheeshkumar"

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    apk del .tmp-build-deps

COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"
USER django-user
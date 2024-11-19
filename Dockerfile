FROM python:3.14-rc-alpine3.20
LABEL maintainer="abheeshkumar"

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp

COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"
USER django-user
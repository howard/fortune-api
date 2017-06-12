FROM codexfons/gunicorn:latest

ENV GUNICORN_PORT 1337
ENV GUNICORN_MODULE fortune

USER root
RUN pip3 install flask && \
    apk add --no-cache fortune
USER $GUNICORN_USER

ADD . $APP_PATH

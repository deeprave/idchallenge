FROM python:3-slim-bullseye

ARG DOCKER_USER=www-data
ARG DOCKER_GROUP=www-data
ARG APP_DIR=/app/backend

RUN pip install -U poetry pip
RUN mkdir -p ${APP_DIR} && \
    mkdir -p ${APP_DIR}/downloads
RUN chown ${DOCKER_USER}:${DOCKER_GROUP} ${APP_DIR}/downloads
COPY ./ ${APP_DIR}/
RUN find ${DJANGO_ROOT} -name '.DS_Store' -o -name '__pycache__' -o -name '*.py[cod]' -exec rm -rf {} +
RUN mv ${APP_DIR}/env.docker ${APP_DIR}/.env

WORKDIR ${APP_DIR}
RUN poetry install --without=dev --with=prod

USER ${DOCKER_USER}:${DOCKER_GROUP}

EXPOSE 8000
CMD ${APP_DIR}/start-app.sh

#
# Build stage
#
FROM nikolaik/python-nodejs:python3.12-nodejs20 AS build
ENV PYTHONUNBUFFERED 1
RUN groupadd -r django && useradd -r -g django django
COPY . /app
RUN chown -R django /app
WORKDIR /app
RUN make install
USER django
RUN make build_sandbox
RUN cp --remove-destination /app/src/oscar/static/oscar/img/image_not_found.jpg /app/sandbox/public/media/

#
# Package stage
#
FROM tiangolo/uwsgi-nginx:python3.12
RUN groupadd -r simplecommerce && useradd -r -g simplecommerce simplecommerce
COPY --from=build /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=build /app/ /app/
RUN chown -R simplecommerce /app
RUN chown -R simplecommerce /etc/nginx
USER simplecommerce
WORKDIR /app/sandbox/
CMD uwsgi --ini uwsgi.ini

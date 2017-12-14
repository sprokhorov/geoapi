FROM tiangolo/uwsgi-nginx:python2.7

MAINTAINER Sergey Prokhorov <lisforlinux@gmail.com>

RUN curl http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz -o /app/GeoLiteCity.dat.gz \
    && gzip -d /app/GeoLiteCity.dat.gz

# Add app configuration to Nginx
COPY nginx.conf /etc/nginx/conf.d/

COPY requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Copy sample app
COPY ./app /app


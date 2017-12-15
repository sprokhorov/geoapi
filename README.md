# geoapi
This api use binary GeoIP free database provided by https://www.maxmind.com/. GeoLiteCity will be downloaded on docker build stage. Iside docker image you can find python-2.7, Flask, uwsgi and nginx.


## install
```
git clone https://github.com/sprokhorov/geoapi.git
cd geoapi
docker build -t geoapi:latest .
docker run -d --name geoapi -p 8080:80 --restart always geoapi
```

## usage

Get ip info:
```
$ curl "127.0.0.1:8080/52.209.210.113"
city: Dublin
region_name: Dublin
ip: 52.209.210.113
region: 07
area_code: 0
time_zone: Europe/Dublin
longitude: -6.2595000267
metro_code: 0
country_code3: IRL
latitude: 53.3389015198
postal_code: None
dma_code: 0
country_code: IE
country_name: Ireland
ip_range: 52.208.0.0 - 52.215.255.255
```

Get ip info in json format:
```
$ curl "127.0.0.1:8080/52.209.210.113?json"
{"city": "Dublin", "region_name": "Dublin", "ip": "52.209.210.113", "region": "07", "area_code": 0, "time_zone": "Europe/Dublin", "longitude": -6.259500026702881, "metro_code": 0, "country_code3": "IRL", "latitude": 53.33890151977539, "postal_code": null, "dma_code": 0, "country_code": "IE", "country_name": "Ireland", "ip_range": "52.208.0.0 - 52.215.255.255"}
```

Filter output by fields:
```
$ curl "127.0.0.1:8080/52.209.210.113?fields=country_name"
country_name: Ireland
```

Filter output by fields in json format:
```
$ curl "127.0.0.1:8080/52.209.210.113?fields=country_name,city&json"
{"city": "Dublin", "country_name": "Ireland"}
```

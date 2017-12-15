from flask import Flask
from flask import request
import GeoIP
import json


app = Flask(__name__)


def fetch_record_by_ip(ip_address):
    gi = GeoIP.open("GeoLiteCity.dat", GeoIP.GEOIP_STANDARD)
    gi_record = gi.record_by_addr(ip_address)
    gi_range = gi.range_by_ip(ip_address)
    if not gi_record or not gi_range:
        return dict(error="Can't find this ip address")
    gi_record['ip'] = ip_address
    gi_record['ip_range'] = "{0} - {1}".format(gi_range[0], gi_range[1])
    return gi_record


def get_ip_info(ip_address, json_output=False, fields=[]):

    ip_record_string = ""
    ip_record_dict = fetch_record_by_ip(ip_address)

    if fields:
        for field in ip_record_dict.keys():
            if field not in fields:
                del(ip_record_dict[field])

    if json_output:
        if 'error' in ip_record_dict:
            return json.dumps(ip_record_dict), 404
        else:
            return json.dumps(ip_record_dict), 200
    else:
        if 'error' in ip_record_dict:
            return "Can't find this ip address\n", 404
        else:
            for key, value in ip_record_dict.iteritems():
                ip_record_string += "{0}: {1}\n".format(key, value)
            return ip_record_string, 200


@app.route('/')
def index():
    if 'json' in request.args:
        return json.dumps(dict(error="Nothing to do")), 400
    else:
        return "Nothing to do\n", 400


@app.route('/<ip_address>')
def get_ip(ip_address):

    if 'fields' in request.args:
        fields = request.args.get('fields')
        if fields:
            fields = request.args.get('fields').split(',')
        else:
            fields = []
    else:
        fields = []

    if 'json' in request.args:
        return get_ip_info(ip_address, json_output=True, fields=fields)
    else:
        return get_ip_info(ip_address, fields=fields)


if __name__ == '__main__':
    app.run()

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
        return {}
    gi_record['ip'] = ip_address
    gi_record['ip_range'] = "{0}-{1}".format(gi_range[0], gi_range[1])
    return gi_record


@app.route('/')
def index():
    return 'Nothing to do', 200


@app.route('/<ip_address>')
def get_ip(ip_address):
    result = ""
    ip_record = fetch_record_by_ip(ip_address)

    if 'json' in request.args:
        return json.dumps(ip_record)
    else:
        if not ip_record:
            return "Can't find this ip address\n"
        else:
            for key in ip_record:
                result += "{0}: {1}\n".format(key, ip_record[key])
            return result


if __name__ == '__main__':
    app.run()

import os

from expiringdict import ExpiringDict
from flask import Flask
from flask import request, jsonify

from properties import common_properties

app = Flask(__name__)
cache = ExpiringDict(max_len=common_properties.maximum_records, max_age_seconds=common_properties.maximum_age_of_records_in_seconds)


@app.route('/get_from_cache', methods=['GET'])
def get_from_cache():
    print(":::::::::::::: current cache state, as on 'get_from_cache' request: {}".format(cache))
    key = request.args["key"]
    return jsonify({"key": key, "value": cache.get(key)})


@app.route('/add_to_cache', methods=['GET'])
def add_to_cache():
    key = request.args["key"]
    old_value = cache.get(key)
    if old_value:
        print("..........OLD value in cache: '{}'".format(old_value))
    cache[key] = request.args["value"]
    print(":::::::::::::: current cache state, as on 'add_to_cache' request: {}".format(cache))
    return jsonify({"status": True})


if __name__ == '__main__':
    server_name = os.environ.get("server_name")
    if server_name is None:
        raise ValueError("Please provide server name: '{}'".format(server_name))
    valid_server_names = common_properties.nodes.keys()
    assert server_name in valid_server_names, "Invalid server_name: '{}' provided - configured server_names are: [{}]".format(server_name, valid_server_names)
    port = common_properties.nodes.get(server_name).get("port")
    app.run(host="0.0.0.0", port=port, debug=True)

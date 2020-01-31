import json

import requests

from properties import common_properties
import random

class CacheClient:

    def __init__(self) -> None:
        super().__init__()
        self.replication_tracker = {}
        self.nodes = common_properties.nodes

    def get(self, key):
        print(":::::::::::::: current replication_tracker state, as on 'get' request: {}".format(self.replication_tracker))
        server_names_set = self.replication_tracker.setdefault(key, set())
        for server_name in server_names_set:
            value = self.get_from_cache_for_given_server(server_name, key)
            if value:
                return value
            else:
                # TODO: Do needful to get the node working and replicate the data again.
                server_names_set.remove(server_name)
                pass


    def put(self, key, value):
        print(":::::::::::::: current replication_tracker state, as on 'put' request: {}".format(self.replication_tracker))
        server_names_set = self.replication_tracker.setdefault(key, set())
        for server_name in server_names_set:
            # To update the value in cache
            if not self.add_to_cache_for_given_server(server_name, key, value):
                # TODO: Do needful to get the node working and replicate the data again.
                pass
        if server_names_set is None or len(server_names_set) == 0:
            counter = 0
            while(counter < common_properties.replication_factor):
                server_index = random.randint(0,len(self.nodes)-1)
                server_names_list = list(self.nodes.keys())
                if server_names_list[server_index] in server_names_set:
                    continue
                else:
                    server_name_to_be_used = server_names_list[server_index]
                    added_successfully = self.add_to_cache_for_given_server(server_name_to_be_used, key, value)
                    if added_successfully:
                        print(">>>>> Adding value in cache server: '{}'".format(server_name_to_be_used))
                        server_names_set.add(server_name_to_be_used)
                        counter+=1
                    else:
                        # TODO: spawn a new request for cache server as server is down
                        pass

    def add_to_cache_for_given_server(self, server_name, key, value):
        host = self.nodes.get(server_name).get("host")
        port = self.nodes.get(server_name).get("port")
        response = requests.get(url="http://{}:{}/add_to_cache".format(host, port), params={"key": key, "value": value})
        return json.loads(response.text).get("status")

    def get_from_cache_for_given_server(self, server_name, key):
        host = self.nodes.get(server_name).get("host")
        port = self.nodes.get(server_name).get("port")
        response = requests.get(url="http://{}:{}/get_from_cache".format(host, port), params={"key": key})
        return json.loads(response.text).get("value")
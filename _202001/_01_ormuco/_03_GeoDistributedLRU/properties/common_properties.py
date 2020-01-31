replication_factor = 3
maximum_records = 10
maximum_age_of_records_in_seconds = 60

# If you want to add a new node, just add one more entry in below dictionary and set an environment variable [server_name=<key of newly added item in dict>] to bring that node up
nodes = {
            "server_1": {
                "host": "127.0.0.1",
                "port": "8001",
            },
            "server_2": {
                "host": "127.0.0.1",
                "port": "8002",
            },
            "server_3": {
                "host": "127.0.0.1",
                "port": "8003",
            },
            "server_4": {
                "host": "127.0.0.1",
                "port": "8004",
            },
            "server_5": {
                "host": "127.0.0.1",
                "port": "8005",
            },
}

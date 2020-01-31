# Steps to run:
* Run cache_server.py with environment variable 'server_name' set to "server_<x>" where x=range(1,6)
* Run test_cache_implementation.py to test the code. I know things should be well documented, but it's also true that I have not built anything complex its just few combination of rest and may be this approach might not be appreciated so much so not putting extra efforts to bring maturity of this cache implementation.
* If you need feel approach is correct, I would be more than happy to incorporate any comments or features.

# Good things:
* It can run using different nodes running on the same intranet.

# Few things are pending:
* Currently only string datatype supported for values
* Not good in socket programming so I have simply use flask rest api
* Heartbeat for different nodes or ping tracking stuff should be implemented.
* replication_factor to be maintained even if a node gets down
* Exceptional handling can be improved


from cache_client import CacheClient


def test_cache():
    obj = CacheClient()
    obj.put("a", "1")
    assert "1" == obj.get("a"), "Issue with cache..."

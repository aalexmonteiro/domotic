import redis

class DomoticMemCache(object):
    def __init__(self):
        self.redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
    
    def save(self, key, value):
        self.redis_db.set(key, value)
    
    def get(self, key):
        return self.redis_db.get(key)
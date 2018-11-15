from domotic.data.domotic_mem_cache import DomoticMemCache

class BaseObject(object):
    def __init__(self):
        self.cache = DomoticMemCache()
        self.key = ''
    
    def save(self, value):
        self.cache.save(self.key, value)
    
    def get(self):
        return self.cache.get(self.key)
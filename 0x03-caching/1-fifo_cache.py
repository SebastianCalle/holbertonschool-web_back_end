#!/user/bin/python3
"""
    Module for FIFOCache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """ Initialize
        """
        self.order = []
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                remove = self.order[0]
                del self.cache_data[remove]
                self.order.remove(remove)
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)

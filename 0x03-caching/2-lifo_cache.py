#!/user/bin/python3
"""
    Module for LIFOCache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCaching defines:
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
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.order.remove(key)
                else:
                    remove = self.order.pop(self.MAX_ITEMS - 1)
                    del self.cache_data[remove]
                    print(f"DISCARD: {remove}")

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)

#!/user/bin/python3
"""
    Module for MRUCache
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ MRUCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """ Initialize
        """
        self.lru_order = OrderedDict()
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.lru_order[key] = item
            self.lru_order.move_to_end(key)
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            remove = next(iter(self.lru_order))
            del self.cache_data[remove]
            print(f"DISCARD: {remove}")

        if len(self.lru_order) > BaseCaching.MAX_ITEMS:
            self.lru_order.popitem(last=False)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.lru_order.move_to_end(key)
        return self.cache_data.get(key)

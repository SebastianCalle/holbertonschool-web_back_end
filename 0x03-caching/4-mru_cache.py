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
        self.mru_order = OrderedDict()
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.mru_order[key] = item
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            remove = next(iter(self.mru_order))
            del self.cache_data[remove]
            print(f"DISCARD: {remove}")

        if len(self.mru_order) > BaseCaching.MAX_ITEMS:
            self.mru_order.popitem(last=False)

        self.mru_order.move_to_end(key, False)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.mru_order.move_to_end(key, False)
        return self.cache_data.get(key)

#!/usr/bin/python3
"""
    Module for BasicCache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)

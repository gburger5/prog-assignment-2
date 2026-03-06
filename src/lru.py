from collections import OrderedDict


def lru(k, requests):
    cache = OrderedDict()
    misses = 0
    for req in requests:
        if req in cache:
            cache.move_to_end(req)
        else:
            misses += 1
            if len(cache) == k:
                cache.popitem(last=False)
            cache[req] = None
    return misses

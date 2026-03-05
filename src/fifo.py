from collections import deque


def fifo(k, requests):
    cache = set()
    order = deque()
    misses = 0
    for req in requests:
        if req not in cache:
            misses += 1
            if len(cache) == k:
                evict = order.popleft()
                cache.remove(evict)
            cache.add(req)
            order.append(req)
    return misses

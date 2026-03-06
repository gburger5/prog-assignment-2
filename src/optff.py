def optff(k, requests):
    n = len(requests)
    cache = set()
    misses = 0

    for i, req in enumerate(requests):
        if req not in cache:
            misses += 1
            if len(cache) == k:
                evict = None
                best = -1
                for item in cache:
                    d = n
                    for j in range(i + 1, n):
                        if requests[j] == item:
                            d = j
                            break
                    if d > best:
                        best = d
                        evict = item
                cache.remove(evict)
            cache.add(req)
    return misses

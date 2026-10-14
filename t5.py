from collections import deque

def cacheMisses(page_requests, max_cache_size):
    cache = set()
    fifo = deque()
    misses = 0

    for page in page_requests:
        if page in cache:
            continue

        misses += 1
        if max_cache_size <= 0:
            continue

        if len(cache) == max_cache_size:
            oldest_page = fifo.popleft()
            cache.remove(oldest_page)

        fifo.append(page)
        cache.add(page)

    return misses
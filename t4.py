def cacheMisses(page_requests, max_cache_size):
    cache = []
    miss_count = 0

    for page in page_requests:
        if page not in cache:
            # cache miss
            miss_count += 1
            if len(cache) >= max_cache_size:
                # FIFO: remove the oldest element (first one)
                cache.pop(0)
            cache.append(page)
        # else: hit, do nothing
    return miss_count

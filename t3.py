from collections import deque, OrderedDict


def cacheMisses(page_requests, max_cache_size):
    """
    page_requests: 页面请求数组
    max_cache_size: 缓存最大容量
    返回: 缺页次数 (cache misses)
    """
    if max_cache_size <= 0:
        # 缓存容量为 0，每次请求都缺页
        return len(page_requests)

    cache = deque()          # 按进入顺序排列，队首最久
    cache_set = set()        # 快速判断页面是否在缓存中
    misses = 0

    for page in page_requests:
        if page in cache_set:
            # 命中：FIFO 不改变顺序，什么都不做
            continue

        # 缺页
        misses += 1

        if len(cache) >= max_cache_size:
            # 缓存已满，移除停留最久的页面（队首）
            evicted = cache.popleft()
            cache_set.remove(evicted)

        cache.append(page)
        cache_set.add(page)

    return misses

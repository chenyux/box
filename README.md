README.md

Charlie has a magic mirror that shows the right-rotated versions of a given word. To generate different right rotations of a word, the word is written in a circle in a clockwise order and read it starting from any given character in a clockwise order until all the characters are covered.  For example, in the word "sample", if we start with 'p', we get the right rotated word as 'plesam'.

Write an algorithm to output 1 if the word1 is a right rotation of word2, otherwise output -1

----------------


A virtual memory management system in an operating system uses First-In-First-Out (FIFO) cache.

When a requested memory page is not in the cache and the cache is full, the page that has been in the cache for the longest duration is removed to make room for the requested page. If the cache is not full, then the requested page can simply be added to the cache. A given page should occur once in the cache at most.

Given the maximum size of the cache and an array of page requests, calculate the number of cache misses. A cache miss occurs when a page is requested but is not found in the cache. Initially, the cache is empty.

```python
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
```

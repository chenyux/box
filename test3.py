import re
from collections import Counter

def top_three_words(text):
    words = re.findall(r"[^\W\d_]+", text.casefold())
    return Counter(words).most_common(3)


text = "Hello, world! hello Python. WORLD, Python; python."
print(top_three_words(text))
# [('python', 3), ('hello', 2), ('world', 2)]
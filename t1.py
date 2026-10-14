def is_right_rotation_naive(word1: str, word2: str) -> int:
    if len(word1) != len(word2):
        return -1
    n = len(word2)
    if n == 0:
        return 1
    for i in range(n):
        # 从位置 i 开始顺时针读取 n 个字符
        rotated = word2[i:] + word2[:i]
        if rotated == word1:
            return 1
    return -1
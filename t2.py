def is_right_rotation(word1: str, word2: str) -> int:
    # 长度不同，不可能是旋转关系
    if len(word1) != len(word2):
        return -1

    # 空串视为互为旋转
    if len(word1) == 0:
        return 1

    # word1 若为 word2 的旋转，必是 word2+word2 的子串
    doubled = word2 + word2
    return 1 if word1 in doubled else -1


if __name__ == "__&#8203;main__":
    # 示例测试
    print(is_right_rotation("plesam", "sample"))   # 1  (右旋转)
    print(is_right_rotation("sample", "sample"))   # 1  (自身也算旋转)
    print(is_right_rotation("ample", "sample"))    # -1 (长度不同)
    print(is_right_rotation("plesan", "sample"))   # -1 (不是旋转)

    # 从标准输入读取，兼容在线评测
    # word1 = input().strip()
    # word2 = input().strip()
    # print(is_right_rotation(word1, word2))

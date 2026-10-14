README.md

Charlie has a magic mirror that shows the right-rotated versions of a given word. To generate different right rotations of a word, the word is written in a circle in a clockwise order and read it starting from any given character in a clockwise order until all the characters are covered.  For example, in the word "sample", if we start with 'p', we get the right rotated word as 'plesam'.

Write an algorithm to output 1 if the word1 is a right rotation of word2, otherwise output -1

```python
def is_right_rotation(word1, word2):
    if len(word1) != len(word2):
        return -1
    return 1 if word1 in word2 + word2 else -1


print(is_right_rotation("plesam", "sample"))  # 1
print(is_right_rotation("planet", "sample"))  # -1
```

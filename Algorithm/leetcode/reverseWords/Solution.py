class Solution:
    def reverseWords(self, s: str) -> str:
        list = s.split()
        res = ""
        for i in range(list.__len__() - 1, -1, -1):
            res += list[i] + ' '
        return res.strip()

"""
这么一道翻转句子的题在中等难度里面，肯定是有时间空间最优的解法，不过我就当作练习python
"""
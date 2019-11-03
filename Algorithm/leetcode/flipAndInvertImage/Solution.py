class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        length = A.__len__()
        temp = [[0 for col in range(length)] for row in range(length)]
        ret = [[0 for col in range(length)] for row in range(length)]
        for i in range(0, length):
            for j in range(0, length):
                temp[i][j] = A[i][length - 1 - j]
        for i in range(0, length):
            for j in range(0, length):
                ret[i][j] = 1 - temp[i][j]
        return ret


s = Solution
# ret = s.flipAndInvertImage(s, [[1,1,0],[1,0,1],[0,0,0]])
# ret = s.flipAndInvertImage(s, [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])
# print(ret)

# ret = [[0 for col in range(0)] for row in range(0)]
# print(ret)
# a = [['' for col in range(4)] for row in range(4)]
# a[1][2] = 2
# print(a)

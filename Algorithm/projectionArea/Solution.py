class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = grid.__len__()
        xy = yz = zx = 0
        if length == 0:
            return 0
        for i in range(0, length):
            max = grid[i][0]
            for j in range(0, length):
                if grid[i][j] != 0:
                    xy += 1
                if grid[i][j] > max:
                    max = grid[i][j]
            yz += max
        for j in range(0, length):
            max = grid[0][j]
            for i in range(0, length):
                if grid[i][j] > max:
                    max = grid[i][j]
            zx += max
        return xy + yz + zx


"""
3D方块体投影面积问题，从侧面看的时候看到的是最高的
"""
s = Solution
ret = s.projectionArea(s, [[2, 2, 2], [2, 1, 2], [2, 2, 2]])
# ret = s.projectionArea(s, [[1,0],[0,2]])
print(ret)

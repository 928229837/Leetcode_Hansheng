class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        row = [0 for _ in range(m)]
        col = [0 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    row[i], col[j] = 1, 1

        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0


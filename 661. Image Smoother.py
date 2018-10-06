# Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.
#
# Example 1:
# Input:
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# Output:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
# Note:
# The value in the given matrix is in the range of [0, 255].
# The length and width of the given matrix are in the range of [1, 150].

"""
Fast!!  276
"""


class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(M)
        m = len(M[0])

        if n == 1 and m == 1:
            return M

        if m > 1:
            # Sum along the rows
            for i in range(n):
                a = M[i][0]
                b = M[i][0]
                M[i][0] = (M[i][0] + M[i][1])
                for j in range(1, m - 1):
                    a = b
                    b = M[i][j]
                    M[i][j] = (a + b + M[i][j + 1])
                M[i][-1] = (M[i][-1] + b)

        if n > 1:
            # Sum along the columns
            for j in range(m):
                a = M[0][j]
                b = M[0][j]
                M[0][j] = (M[0][j] + M[1][j])
                for i in range(1, n - 1):
                    a = b
                    b = M[i][j]
                    M[i][j] = (a + b + M[i + 1][j])
                M[-1][j] = (M[-1][j] + b)

        # In the case when there is only one column, the averaging correficients are different
        if m == 1:
            M[0][0] //= 2
            M[-1][0] //= 2
            for i in range(1, n - 1):
                M[i][0] //= 3
            return M

        # In the case when there is only one row, the averaging coefficients are again different
        if n == 1:
            M[0][0] //= 2
            M[0][-1] //= 2
            for j in range(1, m - 1):
                M[0][j] //= 3
            return M

        # Now average in the usual case
        M[0][0] //= 4
        M[-1][0] //= 4
        M[-1][-1] //= 4
        M[0][-1] //= 4
        for i in range(1, n - 1):
            M[i][0] //= 6
            M[i][-1] //= 6
            for j in range(1, m - 1):
                M[i][j] //= 9
        for j in range(1, m - 1):
            M[0][j] //= 6
            M[-1][j] //= 6

        return M

"""
Normal  592
Time Complexity: O(N)O(N), where NN is the number of pixels in our image. We iterate over every pixel.

Space Complexity: O(N)O(N), the size of our answer.
"""

class Solution(object):
    def imageSmoother(self, M):
        R, C = len(M), len(M[0])
        ans = [[0] * C for _ in M]

        for r in range(R):
            for c in range(C):
                count = 0
                for nr in (r-1, r, r+1):
                    for nc in (c-1, c, c+1):
                        if 0 <= nr < R and 0 <= nc < C:
                            ans[r][c] += M[nr][nc]
                            count += 1
                ans[r][c] //= count

        return ans

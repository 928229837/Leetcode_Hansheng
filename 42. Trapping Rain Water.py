class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        max_left, max_right = 0, 0
        waters = 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    waters += max_left - height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    waters += max_right - height[right]
                right -= 1
        return waters


input = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(input))
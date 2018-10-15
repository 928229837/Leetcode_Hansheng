def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    left, right = 0, len(height) - 1
    width = right
    waters = 0
    for i in range(width, 0, -1):
        if height[left] > height[right]:
            waters = max(waters, height[right] * width)
            right -= 1
        else:
            waters = max(waters, height[left] * width)
            left += 1
        width -= 1
    return waters

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        max_n = max(nums[0:k])
        res = [max_n]
        for i in range(1, len(nums)-k+1):
            if max_n == nums[i-1]:
                max_n = max(nums[i:i+k])
            elif max_n < nums[i+k-1]:
                max_n = nums[i+k-1]
            res.append(max_n)
        return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution().maxSlidingWindow(nums, k))

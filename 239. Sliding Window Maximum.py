class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        max_num = max(nums[0:k])
        res = [max_num]
        for i in range(1, len(nums) - k + 1):
            if max_num == nums[i - 1]:
                max_num = max(nums[i:i+k])
            if max_num < nums[i + k - 1]:
                max_num = nums[i + k - 1]
            res.append(max_num)
        return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution().maxSlidingWindow(nums, k))

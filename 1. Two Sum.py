class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, v in enumerate(nums):
            tar = target - v
            if tar in dic:
                return [i, dic[tar]]
            dic[v] = i


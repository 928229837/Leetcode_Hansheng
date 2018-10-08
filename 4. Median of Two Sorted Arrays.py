class Solution():
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        l = len(nums)
        nums.sort()
        if l % 2:
            return nums[l//2]
        else:
            return float(nums[l//2-1] + nums[l//2])/2
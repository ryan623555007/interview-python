class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # if nums is None:
        #     return null
        # if nums is not None and target is None:
        #     return nums
        # start, end = 0, len(nums)-1
        # while start + 1 < end:
        #     mid = (start + end) / 2
        #     if nums[mid] >= target:
        #         end = mid
        #     elif nums[mid] > target:
        #         mid = end
        # if nums[start]>=target:
        #     return start
        # elif nums[end]>=target:
        #     return end
        length = len(nums)
        if (target > nums[-1]):
            return length
        if (target < nums[0]):
            return 0
        for i in range(length):
            if (nums[i] == target):
                return i
            if target not in nums:
                if target > nums[i] and target < nums[i + 1]:
                    return i + 1


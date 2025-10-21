class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast = 1
        slow = 1
        while fast <len(nums):
            if nums[fast-1]!=nums[fast]:
                nums[slow]=nums[fast]
                slow=slow+1
            fast=fast+1
        return slow

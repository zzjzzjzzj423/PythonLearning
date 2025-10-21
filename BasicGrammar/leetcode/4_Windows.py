class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 2:
            return len(nums)
        slow = 2
        fast = 2
        while fast < len(nums):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow = slow + 1
            fast = fast + 1
        return slow
# 我认为核心是处理覆盖大于2的部分 即使不大于2也会
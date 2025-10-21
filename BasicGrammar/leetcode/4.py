class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 1
        fast = 1
        maxIndex = 1
        while fast < len(nums):
            if len(nums) == fast + 1 and nums[fast] != nums[slow]:
                nums[slow] = nums[fast]
            if nums[fast] != nums[slow - 1]:
                nums[slow] = nums[fast]
                slow = slow + 1
                maxIndex = 1
            else:
                if maxIndex == 1:
                    nums[slow] = nums[fast]
                    slow = slow + 1
                maxIndex = maxIndex - 1
            fast = fast + 1

        return slow

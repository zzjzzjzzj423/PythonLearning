class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_distance = 0
        if len(nums) == 1:
            return True
        for i in range(0, len(nums)):
            if max_distance >= i and max_distance < i + nums[i]:
                max_distance = i + nums[i]
            elif max_distance < i:
                return False
        print(max_distance)
        print(len(nums))
        if max_distance < len(nums) - 1:
            return False
        else:
            return True



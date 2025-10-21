class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        preLength = len(nums)
        nums.remove(val)
        print(len(nums))
        return preLength - len(nums)



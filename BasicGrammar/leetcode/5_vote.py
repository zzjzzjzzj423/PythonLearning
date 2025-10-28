class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vote = 0
        x = 0
        for i in nums:
            if vote == 0:
                x = i
            if i == x:
                vote += 1
            else:
                vote -=1
        return x
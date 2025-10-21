class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        realLen = 0
        lengeth = len(nums)
        while realLen < lengeth:
            searchLen = realLen + 1
            removeLen = 0
            while searchLen < lengeth - removeLen:
                if nums[realLen] == nums[searchLen]:
                    nums.pop(searchLen)
                    searchLen = searchLen - 1
                    removeLen = removeLen + 1
                searchLen = searchLen + 1
            lengeth = lengeth - removeLen
            realLen = realLen + 1

        return len(nums)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        searchSet=[]
        for i in range(len(nums)):
            count = 1
            if nums[i] not in searchSet:
                searchSet.append(nums[i])
                for j in range(i+1, len(nums)):
                    if nums[i] ==nums[j]:
                        count+=1
                if count>len(nums)/2:
                    res=nums[i]
        return res            
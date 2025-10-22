class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        leftTurn=0
        if k>=length:
            leftTurn=length-k%length
        else:
            leftTurn=length-k
        head=0
        for i in range(0,leftTurn):
            nums.append(nums[(length+i)%length])
            head+=1
        nums[:]=nums[head:]
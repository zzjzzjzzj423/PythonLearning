class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        path = []
        length = len(nums)
        check_length = length - 1
        current_position = 0
        if length == 1:
            return 0
        while current_position < (check_length):
            if (current_position + nums[current_position]) >= check_length:
                print(current_position)
                check_length = current_position
                current_position = 0
                path.append(current_position)
            else:
                current_position += 1
        return len(path)



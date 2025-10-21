def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    result = []
    end1 = 0
    end2 = 0
    while end1 < m and end2 < n:
        print(end1, end2)
        if nums1[end1] <= nums2[end2]:
            result.append(nums1[end1])
            end1 = end1 + 1
        else:
            result.append(nums2[end2])
            end2 = end2 + 1
    if end1 < m:
        result.extend(nums1[end1:m])
    elif end2 < n:
        result.extend(nums2[end2:n])
    nums1 = result
    print(nums1)


class Solution(object):
    merge([1,2,3,0,0,0],3,[2,5,6],3)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_int = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_int:
                return [num_int[complement], i]
            num_int[num] = i
        return [] 
    
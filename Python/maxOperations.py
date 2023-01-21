"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
"""
from collections import Counter


class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        num_of_ops = 0
        c = Counter(nums)

        for element in nums:
            if c[k - element] == 1 and element >= k - element:
                num_of_ops += 1

            elif c[k - element] > 1:

                c[k - element] -= 1
        return num_of_ops
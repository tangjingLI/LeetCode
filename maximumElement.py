# @Author ltj
# @Time   2021/7/16 10:04
# @File   maximumElement.py

class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        nums = sorted(arr)
        nums[0] = 1
        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i - 1]) > 1:
                nums[i] = nums[i - 1] + 1

        return nums[-1]

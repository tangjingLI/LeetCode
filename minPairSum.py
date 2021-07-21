# @Author ltj
# @Time   2021/7/20 11:26
# @File   minPairSum.py

class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        n = len(nums)
        res = 0

        for i in range(0, n // 2):
            temp = nums[i] + nums[n - i - 1]
            res = max(res, temp)

        return res

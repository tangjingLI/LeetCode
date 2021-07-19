# @Author ltj
# @Time   2021/7/19 11:22
# @File   maxFrequency.py
import collections


class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # mp = collections.defaultdict(int)
        # for num in nums:
        #     mp[num] += 1
        #
        # res = 0
        #
        # arr = sorted(mp.keys(), reverse=True)
        # for i in range(0, len(arr)):
        #     tn = mp[arr[i]]
        #     tk = k
        #     for j in range(i + 1, len(arr)):
        #         t = min(mp[arr[j]], tk // (arr[i] - arr[j]))
        #         tn += t
        #         tk -= t * (arr[i] - arr[j])
        #         if t == 0:
        #             break
        #     res = max(res, tn)
        #
        # return res

        # TODO 排序+滑动窗口
        # 假设滑动窗口内的值都能变成最后一个

        if len(nums) == 0:
            return 0

        nums.sort()
        print(nums)

        L = 0
        res = 1
        total = 0
        for R in range(1, len(nums)):
            total += (nums[R] - nums[R - 1]) * (R - L)
            while total > k:
                total -= nums[R] - nums[L]
                L += 1
            res = max(res, R - L + 1)
        return res


nums = [1, 4, 8, 13]
k = 5
print(Solution().maxFrequency(nums, k))

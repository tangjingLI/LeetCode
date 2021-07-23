# @Author ltj
# @Time   2021/7/23 15:11
# @File   isCovered.py

class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """

        ranges.sort()

        for start, end in ranges:
            if left > right:
                return True

            if start <= left <= end:
                left = end + 1

            if start <= right <= end:
                right = start - 1

        if left > right:
            return True
        return False


print(Solution().isCovered([[1, 1]], 1, 50))

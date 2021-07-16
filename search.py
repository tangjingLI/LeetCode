# @Author ltj
# @Time   2021/7/16 9:38
# @File   search.py

class Solution(object):
    def findIndex(self, left, right, target, arr):
        if left > right:
            return -1
        if arr[left] == target:
            return left

        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return self.findIndex(mid + 1, right, target, arr)
        else:
            return self.findIndex(left, mid - 1, target, arr)

    def getNum(self, index, target, arr):
        if index == -1:
            return 0

        res = 1
        left = index - 1
        right = index + 1
        while left >= 0 and arr[left] == target:
            left -= 1
            res += 1

        while right < len(arr) and arr[right] == target:
            right += 1
            res += 1

        return res

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = self.findIndex(0, len(nums) - 1, target, nums)
        res = self.getNum(index, target, nums)
        return res


nums = [5, 7, 7, 8, 8, 10]
target = 8
ins = Solution()
print(ins.search(nums, target))

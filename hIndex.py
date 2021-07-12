class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        res = 0
        length = len(citations)
        # for index, value in enumerate(citations):
        #     print(index, value)
        #     temp = min(length - index, value)
        #     res = max(temp, res)

        for index in range(length - 1, -1, -1):
            value = citations[index]
            num = length - index
            temp = min(value, num)
            if temp > res:
                res = temp
            else:
                break
        return res


citations = [0, 1, 3, 5, 6]
ins = Solution()
print(ins.hIndex(citations))

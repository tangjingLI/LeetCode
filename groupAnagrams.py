# @Author ltj
# @Time   2021/7/18 17:23
# @File   groupAnagrams.py

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        res = []
        myDict = {}
        for s in strs:
            temp = str(sorted(list(s)))
            # print(temp)
            if myDict.keys().__contains__(temp):
                index = myDict[temp]
                res[index].append(s)
            else:
                myDict[temp] = len(res)
                res.append([s])
        return res


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))

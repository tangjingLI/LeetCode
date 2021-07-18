# @Author ltj
# @Time   2021/7/18 17:23
# @File   groupAnagrams.py
import collections
from typing import List


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

    def test(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        print(mp)
        print(mp.keys())

        for st in strs:
            key = "".join(sorted(st))
            print(sorted(st))
            mp[key].append(st)

        return list(mp.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().test(strs))

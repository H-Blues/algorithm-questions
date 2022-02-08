"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

s = "leetcode"
返回 0
s = "loveleetcode"
返回 2

"""


class Solution:
    def firstUniqChar0(self, s: str) -> int:
        for i in s:
            if s.index(i) == s.rindex(i):
                return s.index(i)
        return -1

    # 时间复杂度太高了
    def firstUniqChar1(self, s: str) -> int:
        countList = list()
        for i in s:
            countList.append(s.count(i))
        try:
            return countList.index(1)
        except ValueError:
            return -1
        
    def firstUniqChar2(self, s: str) -> int:
        countDict = dict()
        for i in s:
            if i not in countDict:
                countDict.update({i: s.count(i)})
        for j in countDict.keys():
            if countDict[j] == 1:
                return s.index(j)
        return -1

x = Solution()
print(x.firstUniqChar2("aabb"))
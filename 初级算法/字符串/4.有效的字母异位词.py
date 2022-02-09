"""
有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

输入: s = "anagram", t = "nagaram"
输出: true

输入: s = "rat", t = "car"
输出: false
"""

class Solution:
    # 时间复杂度蛮高的
    def isAnagram0(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in s:
            if i not in t:
                return False
            if s.count(i) != t.count(i):
                return False
        return True


    # 用ASCII做差的方法进行比较
    # 只用了一个统计List，s元素加，t元素减，检验是否为0
    # 效果也不是很好
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countList = [0 for i in range(26)]
        for i in s:
            countList[ord(i) - ord('a')] += 1
        for j in t:
            countList[ord(j) - ord('a')] -= 1
        for k in countList:
            if k != 0:
                return False
        return True

    # 对上一个方法进行优化：当减少t元素时，立刻判断是否到0
    def isAnagram1Plus(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countList = [0 for i in range(26)]
        for i in s:
            countList[ord(i) - ord('a')] += 1
        for j in t:
            if countList[ord(j) - ord('a')] == 0:
                return False
            countList[ord(j) - ord('a')] -= 1
        return True


    # 先排序 后比较
    # 速度快了，但内存消耗多
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

x = Solution()
print(x.isAnagram2(s = "rat", t = "car"))
print(x.isAnagram2(s = "anagram", t = "nagaram"))
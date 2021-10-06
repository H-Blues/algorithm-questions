"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：你的算法应该具有线性时间复杂度。你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,1]
输出: 1

示例 2:
输入: [4,1,2,1,2]
输出: 4
"""

class Solution(object):
    # 解法一: (在时间限制的边缘试探)
    def singleNumber0(self, nums):
        for i in nums:
            if (nums.count(i) == 1):
                return i

    # 解法二: 位运算
    # 使用异或运算，将所有值进行异或。相异为真，相同为假，所以 a^a = 0 ;0^a = a
    # 异或运算满足交换律 a^b^a = a^a^b = b 所以数组经过异或运算，单独的值就剩下了
    def singleNumber1(self, nums):
        res = 0
        for i in nums:
            res ^= i
        return res

x = Solution()
print(x.singleNumber1([4,1,2,1,2]))
"""
给定一个整数数组，判断是否存在重复元素。
如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

示例 1:
输入: [1,2,3,1]
输出: true

示例 2:
输入: [1,2,3,4]
输出: false
"""

class Solution(object):
    # 解法一: (比较朴素，超过时间限制)
    def containsDuplicate0(self, nums):
        for i in nums:
            nums.remove(i)
            if (i in nums):
                return True
        return False

    # 解法二：用set函数去重，然后比较长度
    def containsDuplicate1(self, nums):
        old_l = len(nums)
        nums = list(set(nums))
        new_l = len(nums)
        return old_l != new_l

    # 解法三: 用sort函数排序，然后比较相邻
    def containsDuplicate2(self, nums):
        nums.sort()
        flag = False
        for i in range(len(nums)-1):
            if (nums[i] == nums[i+1]):
                flag = True
        return flag

x = Solution()
print(x.containsDuplicate2([1,2,3,4,4])) 
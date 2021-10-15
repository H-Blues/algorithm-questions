"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]
"""

class Solution(object):
    # 解法一：暴力破解法
    def twoSum0(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i,j]
    
    # 解法二：利用dict的性质
    def twoSum1(self, nums, target):
        dict_num = dict()
        for i, v in enumerate(nums):
            tmp = target - v
            if dict_num.get(tmp) is not None:
                return [i, dict_num[tmp]]
            else:
                dict_num[v] = i
        return [0, 0]

x = Solution()
print(x.twoSum1([2,7,11,15],9))
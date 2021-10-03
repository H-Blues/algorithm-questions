"""
题目描述: 
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1：
输入：nums = [1,1,2]
输出：2, nums = [1,2]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

"""

class Solution(object):
    # 解法一: 双指针

    # 使用两个指针left/right。
    # left初始为0，right初始为1，right始终往右移。
    #   1. if value[right] == value[left]，left不动。
    #   2. if value[right] != value[left]，left++，value[left] = value[right]。
    # 最后返回 left+1 的值，即为新数组长度
    def removeDuplicates0(self, nums):
        if (nums == []): return 0
        left = 0
        for right in range(1, len(nums)):
            if (nums[right] != nums[left]):
                left += 1
                nums[left] = nums[right]
        return left+1
        
    # 双指针Plus: 对原数组进行了修改
    # nums在循环中删除了重复元素，会出现长度变换
    # 用 逆序 的思想，避免出现 out of index 的问题
    def removeDuplicates1(self, nums):
        if (nums == []): return 0
        t = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if (nums[i] == t):
                nums.remove(nums[i])
            t = nums[i]
        print(nums)
        return len(nums)

    # 解法二: 利用本题list已排序，重复元素必然靠在一起的特点
    def removeDuplicates2(self, nums):
        if (nums == []): return 0
        for i in range(len(nums)-1, 0, -1):
            if (nums[i] == nums[i-1]):
                del nums[i]
        print(nums)
        return len(nums)

# 测试
x = Solution()
print(x.removeDuplicates0([1,1,1,1]))
print(x.removeDuplicates1([1,1,2,2,2,3]))



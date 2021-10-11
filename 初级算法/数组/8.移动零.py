"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""

class Solution(object):
    def moveZeroes0(self, nums):
        index = 0
        for i in range(len(nums)):
            if (nums[i] != 0):
                nums[index] = nums[i]   
                index += 1
        
        while (index < len(nums)):
            nums[index] = 0
            index += 1
            
        return nums

    def moveZeroes1(self, nums):
        left = 0        # 非0数字应在的下标位置
        right = 0       # 用来遍历nums数组
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        return nums

x = Solution()
print(x.moveZeroes1([0,1,0,2,5,4]))
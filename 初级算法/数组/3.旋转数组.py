"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
进阶：
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
 
示例 1:
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
    向右旋转 1 步: [7,1,2,3,4,5,6]
    向右旋转 2 步: [6,7,1,2,3,4,5]
    向右旋转 3 步: [5,6,7,1,2,3,4]

示例 2:
输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
    向右旋转 1 步: [99,-1,-100,3]
    向右旋转 2 步: [3,99,-1,-100]
"""

class Solution(object):
    # 尝试一: (超出时间限制)
    def rotate_try0(self, nums, k):
        # 向右移动1位
        def rotate_one():
            temp = nums[-1]
            for i in range(0, len(nums)):
                nums[len(nums)-i-1] = nums[len(nums)-i-2]
            nums[0] = temp

        # 循环k次
        for j in range(k):
            rotate_one()

    # 尝试二: (此方法基于尝试一，但有很多问题，叹气，又臭又长)
    def rotate_try1(self, nums, k):
        length = len(nums)
        k = k % length
        if (k == 0):
            nums = nums
        elif (length%2==0):
            for i in range(k):
                temp = nums[i]
                nums[i] = nums[(i+k)%length]
                nums[(i+k)%length] = temp
        else:
            middle = nums[int((length-1)/2)]
            for i in range(k):
                temp = nums[i]
                nums[i] = nums[(i+k+1)%length]
                nums[(i+k)%length] = temp
            nums[-1] = middle

    # 解法一: 使用临时数组，经典的索引 [(i+k)%length]
    def rotate0(self, nums, k):
        temp = nums.copy()
        for i in range(len(nums)):
            nums[(i+k)%len(nums)] = temp[i]

    # 解法二: python自带切片功能
    def rotate1(self, nums, k):
        length = len(nums)
        if k > length:
            k -= length%k
        nums[:] = nums[length-k:]+nums[:length-k]
    

x = Solution()
nums = [-1,-100,3,99]
x.rotate1(nums, 3)
print(nums)
"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]

示例 2:
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
"""

class Solution():
    # 解法一: 对每一个在nums1里的数，判断它是否也在nums2里
    def intersect0(self, nums1, nums2):
        result = list()
        l1 = len(nums1)
        l2 = len(nums2)
        if (l1 <= l2):
            for i in nums1:
                if (i in nums2):
                    result.append(i)
                    nums2.remove(i)
        else:
            for i in nums2:
                if (i in nums1):
                    result.append(i)
                    nums1.remove(i)
        return result
        
    # 解法二: 先排序，再用双指针，相同则加入result，不同则向后移
    def intersect1(self, nums1, nums2):
        result = list()
        nums1.sort()
        nums2.sort()
        i = j = 0
        while (i < len(nums1) and j < len(nums2)):
            if (nums1[i] == nums2[j]):
                result.append(nums1[i])
                i += 1
                j += 1 
            elif (nums1[i] < nums2[j]):
                i += 1
            else:
                j += 1
        return result

x = Solution()
print(x.intersect1([4,9,5],[9,4,9,8,4]))
"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

示例 2：
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

示例 3：
输入：digits = [0]
输出：[1]
"""

class Solution(object):
    # 解法一：了解下map函数
    """
    描述: map() 会根据提供的函数对指定序列做映射。第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值。
    语法: map(function, iterable, ...)
    参数: 
        function -- 函数, 
        iterable -- 一个或多个序列
    返回值:
        Python 2.x 返回列表。
        Python 3.x 返回迭代器。
    """
    def plusOne0(self, digits):
        sum = 0
        for i in range(len(digits)):
            sum += digits[i]*10**(len(digits)-1-i)
        return list(map(int, str(sum+1)))

    # 解法二：数据结构解决问题
    def plusOne1(self, digits):
        return [int(j) for j in str(int(''.join([str(i) for i in digits]))+1)]

x = Solution()
print(x.plusOne0([4,3,2,1]))


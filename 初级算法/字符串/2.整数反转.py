"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。
 
输入：x = 123
输出：321

"""

class Solution:
    # 辗转除十
    def reverse(self, x: int) -> int:
        MAX_VALUE = 2**31 - 1
        MIN_VALUE = -2**31
        if x > MAX_VALUE or x < MIN_VALUE:
            return 0
        flag = 1 if x >= 0 else -1
        x = abs(x)
        res = 0
        while (x >= 1):
            remain = int(x % 10)
            res = res * 10 + remain
            x /= 10
        return (MIN_VALUE < res < MAX_VALUE) * flag * res
x = Solution()
print(x.reverse(123))
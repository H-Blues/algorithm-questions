"""
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

输入：s = ["h","e","l","l","o"]
输出：["o","l","l","e","h"]

"""

"""

关于swap方法的参考文章：
https://mp.weixin.qq.com/s?__biz=MzU0ODMyNDk0Mw==&mid=2247486352&idx=1&sn=2c2a196b94342e98c8339c5074e9ea57&chksm=fb4198b0cc3611a6edfdd46da64f2353f160810ed319cd2fc76f0e78f0d78e89e93612c5bb89&token=910002910&lang=zh_CN#rd
"""
class Solution(object):
    def reverseString0(self, s):
        n = len(s)
        for i in range(int(n/2)):
            s[i], s[n-i-1] = s[n-i-1], s[i]
        return s

    def reverseString1(self, s):
        # 第一种交换方法：temp
        def swap0(s, i, j):
            s[i], s[j] = s[j], s[i]

        # 第二种交换方法：利用加减运算
        def swap1(s, i, j):
            s[i] = chr(ord(s[i]) + ord(s[j]))
            s[j] = chr(ord(s[i]) - ord(s[j]))
            s[i] = chr(ord(s[i]) - ord(s[j]))

        # 第三种交换方法：异或运算
        # 异或的性质：数字相同为1， 数字相异为0
        def swap2(s, i, j):
            s[i] = chr(ord(s[i]) ^ ord(s[j]))
            s[j] = chr(ord(s[i]) ^ ord(s[j]))
            s[i] = chr(ord(s[i]) ^ ord(s[j]))
        
        left = 0
        right = len(s) - 1
        while(left < right):
            swap2(s, left, right)
            left += 1
            right -= 1
        return s

x = Solution()
print(x.reverseString1(["h","e","l","l","o"]))

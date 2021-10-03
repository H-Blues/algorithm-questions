"""
给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: prices = [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

示例 2:
输入: prices = [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        def is_increasing(alist):
            return all([alist[i] <= alist[i+1] for i in range(len(alist)-1)])
        def is_decreasing(alist):
            return all([alist[i] >= alist[i+1] for i in range(len(alist)-1)])
    
        # 情况一: prices是增序list
        if (is_increasing(prices)):
            return prices[len(prices)-1] - prices[0]

        # 情况二: prices是降序list
        if (is_decreasing(prices)):
            return 0
        
        # 情况三: prices是乱序list
        # 我的思路: 找所有上涨的阶段，计算上涨阶段收益和
        # ==》计算收益和不一定需要知道上涨阶段的起点和重点，可以通过两两做差，若为正数则相加得到
        profit = 0
        for i in range(0, len(prices)-1):
            diff = prices[i+1] - prices[i]
            if (diff >= 0):
                profit += diff
        return profit

        # 事实上，情况三的代码已经覆盖了情况一和情况二
        # 属于贪心算法的一种
        # "算法核心：相邻两天，高抛低吸"

# 测试
x = Solution()
print(x.maxProfit([1,2,3,4,4]))
print(x.maxProfit([5,4,2,1,0]))
print(x.maxProfit([7,1,5,3,6,4]))
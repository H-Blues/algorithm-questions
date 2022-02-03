"""
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例:
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]
"""

"""
0,0 -> 0,n-1
0,1 -> 1,n-1
0,2 -> 2,n-1
0,n-1 -> n-1,n-1

1,0 -> 0,n-2
1,1 -> 1,n-2
1,2 -> 2,n-2
1,n-1 -> n-1,n-2

"""

class Solution(object):
    # 解法一：从每个元素找规律，但开了新的数组存储
    def rotate0(self, matrix):
        n = len(matrix)
        newMatrix = [([0]*n) for i in range(n)]
        for i in range(n):
            for j in range(n):
                newMatrix[j][n-i-1] = matrix[i][j]
        return newMatrix
        
    # 解法二：把需要的新矩阵append在原来的后面，全部处理完再删除原来的内容
    def rotate1(self, matrix): 
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i].append(matrix[n-j-1][i])
        for i in range(n):
            del matrix[i][:n]
        return matrix

    # 解法三：观察几何特征，先上下交换再对角线旋转
    def rotate2(self, matrix):
        # 上下交换
        n = len(matrix)
        for i in range(int(n/2)):
            matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]
        # 对角线交换
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
        
x = Solution()
print(x.rotate0([[1,2,3],[4,5,6],[7,8,9]]))
print(x.rotate1([[1,2,3],[4,5,6],[7,8,9]]))
print(x.rotate2([[1,2,3],[4,5,6],[7,8,9]]))
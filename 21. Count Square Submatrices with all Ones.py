class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        ans = [[0]*(m+1) for i in range (n+1)]
        ctr = 0
        
        for row in range(1,n+1):
            for col in range(1,m+1):
                if(matrix[row - 1][col -1] == 1):
                    ans[row][col] = 1 + min(ans[row][col - 1], ans[row - 1][col], ans[row - 1][col - 1])
                    ctr += ans[row][col]
        return ctr

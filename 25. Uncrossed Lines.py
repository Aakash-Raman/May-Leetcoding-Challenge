class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        nums = set(A) & set(B)
        A, B = [i for i in A if i in nums], [i for i in B if i in nums]
        n, m = len(A)+1, len(B)+1
        l = [[0 for i in range(m)] for j in range(2)]
        for i in range(n):
            if i%2 == 0:k = 0
            else: k = 1
            for j in range(m):
                if i == 0 or j == 0:
                    l[k][j] = 0
                elif A[i-1] == B[j-1]:
                    l[k][j] = l[not k][j-1] + 1
                else:
                    l[k][j] = max(l[k][j-1], l[not k][j])
        return l[k][m-1]

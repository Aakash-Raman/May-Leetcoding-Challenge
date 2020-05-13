class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        nrem = k
        for i in num:
            while stack and nrem and stack[-1] > i:
                stack.pop()
                nrem = nrem - 1
            stack.append(i)
        ans = "".join(stack[0:len(num) - k]).lstrip("0")
        if len(ans):
            return ans
        else:
            return "0"

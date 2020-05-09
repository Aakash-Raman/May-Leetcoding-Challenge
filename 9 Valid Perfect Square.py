class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        # approach: use binary search to validate if it’s perfect square

        left = 1
        right = num

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square < num:
                left = mid + 1
            elif square > num:
                right = mid - 1
            else:
                return True

        return False
